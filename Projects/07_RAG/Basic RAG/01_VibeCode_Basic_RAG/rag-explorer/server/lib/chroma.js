import { promises as fs } from 'node:fs'
import path from 'node:path'
import { ChromaClient } from 'chromadb'
import { embedQuery } from './embed.js'

const CHROMA_URL = process.env.CHROMA_URL || 'http://localhost:8000'
const COLLECTION = process.env.CHROMA_COLLECTION || 'vwo_prd'
const LOCAL_STORE_PATH = process.env.LOCAL_DB_PATH || path.resolve(process.cwd(), '..', 'data', '.rag-local-store.json')

const client = new ChromaClient({ path: CHROMA_URL })

// We generate vectors ourselves (via Ollama) and hand them to Chroma, so the
// collection's own embedding function is never called. This custom EF just
// satisfies the client API and would use the same Nomic model if invoked.
const ollamaEF = {
  generate: async (texts) => {
    const { embedTexts } = await import('./embed.js')
    return embedTexts(texts)
  },
}

function normalizeLocalStore(store = {}) {
  return {
    ids: Array.isArray(store.ids) ? store.ids : [],
    documents: Array.isArray(store.documents) ? store.documents : [],
    embeddings: Array.isArray(store.embeddings) ? store.embeddings : [],
    metadatas: Array.isArray(store.metadatas) ? store.metadatas : [],
  }
}

async function readLocalStore() {
  try {
    const raw = await fs.readFile(LOCAL_STORE_PATH, 'utf8')
    return normalizeLocalStore(JSON.parse(raw))
  } catch {
    return normalizeLocalStore({ ids: [], documents: [], embeddings: [], metadatas: [] })
  }
}

async function writeLocalStore(store) {
  await fs.mkdir(path.dirname(LOCAL_STORE_PATH), { recursive: true })
  await fs.writeFile(LOCAL_STORE_PATH, JSON.stringify(store, null, 2))
}

class LocalCollection {
  constructor(store) {
    this.store = normalizeLocalStore(store)
  }

  async add({ ids, documents, embeddings, metadatas }) {
    this.store.ids.push(...ids)
    this.store.documents.push(...documents)
    this.store.embeddings.push(...embeddings)
    this.store.metadatas.push(...metadatas)
    await writeLocalStore(this.store)
  }

  async query({ queryEmbeddings, nResults = 4, include = ['documents', 'metadatas', 'distances'] }) {
    const queryVector = queryEmbeddings?.[0] || []
    const hits = this.store.documents.map((text, index) => ({
      id: this.store.ids[index],
      text,
      metadata: this.store.metadatas[index] || {},
      embedding: this.store.embeddings[index] || [],
    }))

    const scored = hits
      .map((hit) => ({
        ...hit,
        similarity: cosineSimilarity(queryVector, hit.embedding),
      }))
      .filter((hit) => Number.isFinite(hit.similarity))
      .sort((a, b) => b.similarity - a.similarity)
      .slice(0, nResults)

    return {
      ids: [scored.map((hit) => hit.id)],
      documents: [scored.map((hit) => hit.text)],
      metadatas: [scored.map((hit) => hit.metadata)],
      distances: [scored.map((hit) => 1 - hit.similarity)],
    }
  }

  async count() {
    return this.store.documents.length
  }
}

function cosineSimilarity(a, b) {
  if (!Array.isArray(a) || !Array.isArray(b) || !a.length || !b.length || a.length !== b.length) return 0
  const dot = a.reduce((sum, value, index) => sum + value * (b[index] || 0), 0)
  const normA = Math.sqrt(a.reduce((sum, value) => sum + value * value, 0))
  const normB = Math.sqrt(b.reduce((sum, value) => sum + value * value, 0))
  if (!normA || !normB) return 0
  return dot / (normA * normB)
}

export async function getCollection() {
  if (await pingChroma()) {
    return client.getOrCreateCollection({
      name: COLLECTION,
      metadata: { 'hnsw:space': 'cosine', source: 'rag-explorer' },
      embeddingFunction: ollamaEF,
    })
  }

  return new LocalCollection(await readLocalStore())
}

export async function resetCollection() {
  if (await pingChroma()) {
    try {
      await client.deleteCollection({ name: COLLECTION })
    } catch {
      // collection may not exist yet — fine
    }
    return getCollection()
  }

  await writeLocalStore(normalizeLocalStore({ ids: [], documents: [], embeddings: [], metadatas: [] }))
  return new LocalCollection(await readLocalStore())
}

// Stores pre-embedded chunks. ids/documents/embeddings/metadatas are parallel arrays.
export async function storeChunks(collection, { ids, documents, embeddings, metadatas }) {
  if (!collection?.add) throw new Error('Collection object does not expose add()')

  // Chroma caps batch size; 200 is comfortably safe for local.
  const BATCH = 200
  for (let i = 0; i < ids.length; i += BATCH) {
    await collection.add({
      ids: ids.slice(i, i + BATCH),
      documents: documents.slice(i, i + BATCH),
      embeddings: embeddings.slice(i, i + BATCH),
      metadatas: metadatas.slice(i, i + BATCH),
    })
  }
}

// Embeds the query, retrieves top-k, returns normalized results + the query vector.
export async function retrieve(collection, queryText, k = 4) {
  const queryEmbedding = await embedQuery(queryText)
  const res = await collection.query({
    queryEmbeddings: [queryEmbedding],
    nResults: k,
    include: ['documents', 'metadatas', 'distances'],
  })
  const docs = res.documents?.[0] || []
  const metas = res.metadatas?.[0] || []
  const dists = res.distances?.[0] || []
  const ids = res.ids?.[0] || []

  const results = docs.map((text, i) => {
    const distance = dists[i]
    return {
      id: ids[i],
      text,
      metadata: metas[i] || {},
      distance,
      // cosine distance -> similarity in [0,1] for display
      similarity: typeof distance === 'number' ? Math.max(0, 1 - distance) : null,
    }
  })
  return { results, queryEmbedding }
}

export async function countChunks(collection) {
  try {
    return await collection.count()
  } catch {
    return 0
  }
}

export async function pingChroma() {
  try {
    await client.heartbeat()
    return true
  } catch {
    return false
  }
}
