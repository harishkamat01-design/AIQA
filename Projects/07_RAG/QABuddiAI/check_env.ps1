Write-Host "🔍 Checking environment variables..."
Write-Host "GROQ_API_KEY:" ($env:GROQ_API_KEY ? "set" : "not set")
Write-Host "LLM_BASE_URL:" $env:LLM_BASE_URL
Write-Host "LLM_MODEL:" $env:LLM_MODEL
Write-Host "RERANK_MODEL:" $env:RERANK_MODEL
Write-Host "QDRANT_PATH:" $env:QDRANT_PATH
Write-Host "PORT:" $env:PORT
Write-Host ""

Write-Host "⚙️ Checking Groq model availability..."
try {
    $response = Invoke-RestMethod -Uri "$env:LLM_BASE_URL/models" -Headers @{Authorization="Bearer $env:GROQ_API_KEY"}
    if ($response.models -match $env:LLM_MODEL) {
        Write-Host "✅ Groq model $($env:LLM_MODEL) is available"
    } else {
        Write-Host "❌ Groq model not found"
    }
} catch {
    Write-Host "❌ Error connecting to Groq API:" $_.Exception.Message
}

Write-Host ""
Write-Host "🗄️ Checking Qdrant..."
try {
    $qdrant = Invoke-RestMethod -Uri "http://localhost:6333/healthz"
    if ($qdrant.status -eq "ok") {
        Write-Host "✅ Qdrant is running"
    } else {
        Write-Host "❌ Qdrant not running"
    }
} catch {
    Write-Host "❌ Qdrant not reachable"
}

Write-Host ""
Write-Host "🌐 Checking server port $env:PORT..."
$portCheck = Get-NetTCPConnection -LocalPort $env:PORT -ErrorAction SilentlyContinue
if ($portCheck) {
    Write-Host "✅ Something is listening on port $env:PORT"
} else {
    Write-Host "❌ Nothing running on port $env:PORT"
}
