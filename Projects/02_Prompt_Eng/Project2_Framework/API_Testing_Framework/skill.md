---
name: rice-pot-api-framework-builder
description: Build a structured, high-quality AI prompt using the RICE-POT framework (Role, Instructions, Context, Example, Parameters, Output, Tone) for designing a complete API testing framework. Apply this when the user wants to create, structure, or improve an API automation framework prompt — especially for Rest Assured (Java), Python Requests, or Playwright APIRequestContext. Trigger this even if the user only describes "API testing framework" without naming RICE-POT explicitly.

---

# RICE-POT API Framework Prompt Builder

Turn a vague API testing goal into a clean, structured prompt using the **RICE-POT** framework. The job is to **interview the user**, fill in every component, then **assemble a finished prompt they can copy and reuse**.

## What RICE-POT Means

| Letter | Component    | What it captures |
|--------|--------------|------------------|
| **R**  | Role         | The persona the AI should adopt (e.g., "Expert QA Automation Architect") |
| **I**  | Instructions | Step-by-step commands, mandatory rules, and "Don't" lists |
| **C**  | Context      | Background — product, system, API docs, configs |
| **E**  | Example      | A sample test case or snippet showing ideal output |
| **P**  | Parameters   | Constraints on accuracy, determinism, no hallucination |
| **O**  | Output       | The exact artifact and format (code, tables, reports) |
| **T**  | Tone         | The communication style (technical, precise, output-only) |

---

## Workflow

1. **Interview** the user to capture the Objective and all seven components.  
   - Objective: Build a complete API testing framework using RICE-POT principles.  
   - API documentation: https://restful-booker.herokuapp.com/apidoc/index.html  

2. **Assemble** the answers into the RICE-POT template.  
3. **Deliver** the finished prompt in a single copy-pasteable block.  
4. **Refine** based on feedback.

---

## Recommended Parameters Block
- Output must be deterministic (same input → same output).
- Every assertion must be traceable to a provided input or API documentation.
- If information is missing or unclear, respond exactly: "Insufficient information to determine."
- If a detail is inferred, label it exactly: "Inference (low confidence)".
- Do not invent endpoints, payloads, error codes, or behaviors not in the API docs.
- Do not assume default or "typical" system behavior.


---

## Worked Example (API Context)

```markdown
### R — Role
Expert QA Automation Architect with 12+ years’ experience in API testing.

### I — Instructions
1. Define framework architecture using RICE-POT principles.
2. Implement API test cases using Rest Assured (Java) OR Python Requests OR Playwright APIRequestContext.
3. Externalize configuration (base URLs, tokens).
4. Add reporting (Extent, Allure, pytest-html).
5. Integrate with CI/CD (Jenkins, GitHub Actions).
Do NOT:
- Hardcode credentials or endpoints.
- Mix UI and API logic in the same layer.

### C — Context
- Product/system: RESTful Booker API (https://restful-booker.herokuapp.com/apidoc/index.html).
- Inputs: Environment configs, test data files (JSON), schema definitions.

### E — Example
Sample Rest Assured test:
```java
@Test
public void verifyCreateBooking() {
    given()
        .baseUri(config.getBaseUrl())
        .contentType(ContentType.JSON)
        .body(testData.getBookingPayload())
    .when()
        .post("/booking")
    .then()
        .statusCode(200)
        .body("bookingid", notNullValue());
}

P — Parameters
- Output must be deterministic.
- Assertions traceable to API docs.
- No hallucination of endpoints or payloads.
O — Output
- Format: Code snippets (Java/Python/TypeScript) + Markdown tables for test cases.
- Structure: Config files, TestData folder, Utilities, Reports, CI/CD pipeline scripts.
T — Tone
Technical, precise, output-only.





