import fs from 'fs';
import path from 'path';

const dataPath = path.resolve(__dirname, '../data/testdata.json');

export const data = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));

export function getPayload(key: string) {
  return data[key];
}
