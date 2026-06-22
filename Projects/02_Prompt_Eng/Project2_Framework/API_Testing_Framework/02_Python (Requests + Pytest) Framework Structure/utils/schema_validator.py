import json
from jsonschema import validate, ValidationError


class SchemaValidator:
    @staticmethod
    def load_schema(path):
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def validate(response_json, schema_path):
        schema = SchemaValidator.load_schema(schema_path)
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as exc:
            raise AssertionError(f'Schema validation failed: {exc.message}') from exc
