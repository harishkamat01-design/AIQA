# Rest Assured API Testing Framework Structure

This folder contains a Rest Assured-based Java API testing framework skeleton built from the attached RICE POT blueprint.

## Architecture

- `src/test/java` - Java test code and framework helpers
- `src/test/resources` - environment configuration, TestNG suite definitions, shared resources
- `testdata` - external JSON payloads used by API tests
- `schemas` - JSON schema definitions for response validation
- `ci` - CI/CD pipeline definitions, e.g. GitHub Actions workflow
- `pom.xml` - Maven build file with dependencies for Rest Assured, TestNG, and schema validation

## Core framework layers

1. **Configuration**
   - Centralized properties in `src/test/resources/config.properties`
   - `ConfigReader` utility loads environment values

2. **Test base**
   - `TestBase` configures `RestAssured.baseURI` and shared request settings
   - Supports explicit environment control and reusable request behaviors

3. **Test cases**
   - API tests are implemented with TestNG and Rest Assured
   - Assertions are data-driven and traceable to external test payloads

4. **Test data**
   - `testdata/` contains deterministic JSON inputs
   - `schemas/` contains contract definitions for response validation

5. **CI/CD**
   - `ci/github-actions.yml` demonstrates how to run Maven tests in GitHub Actions

## RICE POT alignment

- Role: QA automation architect designing an API framework
- Instructions: externalized configuration, reusable utilities, schema validation, CI integration
- Context: e-commerce REST APIs for login, product catalog, cart, orders
- Example: sample Rest Assured login API test included
- Parameters: deterministic output, explicit config, modular design
- Output: framework structure, config files, test data, CI pipeline

## Getting started

1. Open the folder in IntelliJ or VS Code
2. Run `mvn test -DsuiteXmlFile=src/test/resources/testng.xml`
3. Verify the sample login test passes

## Folder structure

```text
01_Rest Assured (Java) Framework Structure/
├── README.md
├── FrameworkStructure.md
├── pom.xml
├── ci/
│   └── github-actions.yml
├── schemas/
│   └── login_schema.json
├── src/
│   └── test/
│       ├── java/
│       │   └── com/restassured/framework/
│       │       ├── base/TestBase.java
│       │       ├── tests/LoginApiTest.java
│       │       └── utils/ConfigReader.java
│       └── resources/
│           ├── config.properties
│           └── testng.xml
└── testdata/
    └── login_payload.json
```
