import fs from 'fs';
import path from 'path';
import Ajv from 'ajv';

const ajv = new Ajv();

export function validateSchema(data: unknown, schemaFile: string) {
  const schemaPath = path.resolve(__dirname, '../schemas', schemaFile);
  const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf-8'));
  const validate = ajv.compile(schema);

  if (!validate(data)) {
    throw new Error(`Schema validation failed: ${JSON.stringify(validate.errors)}`);
  }
}
