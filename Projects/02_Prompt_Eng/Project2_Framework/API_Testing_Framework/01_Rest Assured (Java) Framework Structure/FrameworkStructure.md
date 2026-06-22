# Framework Blueprint

## Test case matrix

| Area | Test Case | Inputs | Assertions | Data Source |
|---|---|---|---|---|
| Authentication | Verify login API returns valid token | `testdata/login_payload.json` | `statusCode == 200`, `token != null` | JSON payload |
| Catalog | Verify product list retrieval | config endpoint + auth token | `statusCode == 200`, schema validation | config + schema |
| Cart | Add item to cart with valid payload | product data + auth token | `statusCode == 201`, response body contains item | JSON payload |
| Orders | Create order and verify status | order payload | `statusCode == 201`, response contract matches schema | JSON payload |

## Folder responsibilities

- `pom.xml`: Maven dependency and build configuration
- `src/test/resources/config.properties`: externalized environment values
- `testdata/`: deterministic JSON request payloads
- `schemas/`: JSON contract files for response validation
- `ci/github-actions.yml`: CI workflow for Maven test execution
- `src/test/java`: reusable test utilities and API test classes

## Reusable utilities

- `ConfigReader.java`:
  - reads environment settings from properties
  - avoids hardcoded endpoints and credentials
- `TestBase.java`:
  - initializes `RestAssured.baseURI`
  - applies common request settings across tests

## Sample API signature inference

- `/login` - authenticates user and returns `token`
- `/products` - retrieves product catalog
- `/cart` - adds items to shopping cart
- `/orders` - places an order

> Inference (low confidence): these endpoints follow common e-commerce API patterns and match the prompt context.
