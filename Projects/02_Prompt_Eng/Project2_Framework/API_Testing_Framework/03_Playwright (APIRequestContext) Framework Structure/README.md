# Playwright APIRequestContext Framework Structure

This framework skeleton is built with Playwright APIRequestContext and uses RICE POT principles.

## Structure

- `tests/` - API test specifications
- `utils/` - reusable helpers for config, data loading, and schema validation
- `data/testdata.json` - deterministic request payloads
- `schemas/` - JSON response contract definitions
- `playwright.config.ts` - Playwright test configuration
- `reports/allure-results/` - Allure reporting output
- `package.json` - dependencies and scripts

## Run tests

```bash
npm install
npm test
```

## Generate Allure report

```bash
npm run report
```
