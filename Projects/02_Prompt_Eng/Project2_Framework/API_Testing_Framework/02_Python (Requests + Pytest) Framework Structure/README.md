# Python Requests + Pytest API Testing Framework Structure

This framework skeleton is designed with RICE POT principles and uses Python `requests` + `pytest`.

## Structure

- `tests/` - API test modules
- `utils/` - reusable helpers for config, data, logging, and schema validation
- `config/config.yaml` - external environment and endpoint configuration
- `data/testdata.json` - deterministic request payloads
- `schemas/` - JSON response contract definitions
- `reports/pytest_html/` - pytest HTML report output
- `.github/workflows/ci.yml` - CI pipeline for GitHub Actions
- `requirements.txt` - Python dependencies

## Sample test flow

1. Load config via `utils/config_loader.py`
2. Load payloads via `utils/data_loader.py`
3. Call API with `requests`
4. Validate response schema with `utils/schema_validator.py`
5. Use pytest reporting for deterministic validation

## Running tests

```bash
pip install -r requirements.txt
pytest --html=reports/pytest_html/report.html
```
