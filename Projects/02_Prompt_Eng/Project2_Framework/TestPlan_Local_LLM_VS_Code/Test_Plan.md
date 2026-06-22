# Test Plan

## 1. Objective
The objective of this test plan is to verify the Restful Booker API endpoints, including booking creation, update, deletion with authentication, and token-based authorization. The plan aims to identify functional, security, performance, and data integrity issues and document defects for regression and automation coverage.

API Reference: https://restful-booker.herokuapp.com/apidoc/index.html

## 2. Scope
The scope of this test plan includes the following areas:

### 2.1 Functional Testing
- Verify all documented API endpoints.
- Test booking creation, retrieval, update, and deletion.
- Validate authentication and authorization for protected operations.

### 2.2 Data Validation Testing
- Confirm input validation for mandatory fields and types.
- Test boundary and invalid values.
- Verify returned response data accuracy.

### 2.3 Error Handling Testing
- Confirm proper HTTP status codes and error messages.
- Verify no sensitive information is leaked in error responses.
- Check graceful handling of invalid and malformed requests.

### 2.4 Performance Testing
- Measure response times under normal and peak load.
- Identify throughput and scalability constraints.

### 2.5 Security Testing
- Validate authentication and authorization enforcement.
- Check for common security issues such as injection risks.
- Confirm data is transmitted securely over HTTPS.

### 2.6 Integration Testing
- Verify interactions between related endpoints.
- Ensure data consistency across booking operations.

### 2.7 Compatibility Testing
- Confirm the API works across supported client platforms and tools.

### 2.8 Documentation Review
- Validate the API documentation against actual behavior.
- Ensure documented request and response formats are accurate.

### 2.9 Regression and Edge Case Testing
- Re-test existing functionality after fixes.
- Validate boundary, concurrency, and unexpected input scenarios.

## 3. Inclusions
The following test areas and operations are included:

### 3.1 Create (POST)
- Create new bookings with valid payloads.
- Validate error responses for invalid or missing data.
- Confirm data persistence after creation.

### 3.2 Read (GET)
- Retrieve booking details by booking ID.
- Query bookings by supported criteria.
- Validate handling of invalid or missing IDs.

### 3.3 Update (PUT)
- Modify existing bookings with valid updates.
- Confirm invalid updates produce appropriate errors.
- Verify updated data is saved correctly.

### 3.4 Delete (DELETE)
- Delete bookings using valid booking IDs.
- Confirm successful deletion responses.
- Ensure deleted records are no longer accessible.

### 3.5 Boundary Testing
- Test minimum and maximum allowed values.
- Validate behavior near input boundaries.

### 3.6 Concurrency Testing
- Test concurrent CRUD operations.
- Verify data consistency during simultaneous requests.

### 3.7 Data Validation
- Test invalid characters, types, and missing fields.
- Validate API response for malformed inputs.

### 3.8 Authentication and Authorization
- Verify endpoints with authenticated and unauthenticated access.
- Confirm authorization controls for protected operations.

### 3.9 Security Testing
- Validate against injection and other API security risks.
- Confirm that sensitive information is not exposed.

### 3.10 Performance Testing
- Measure latency and throughput for CRUD operations.
- Evaluate API stability under load.

### 3.11 Integration Testing
- Confirm booking workflows across endpoints.
- Validate related operations for data consistency.

### 3.12 Regression Testing
- Re-run tests after changes to ensure no regressions.

### 3.13 Documentation Review
- Ensure documentation is complete and accurate.

### 3.14 Load and Rate Limiting Testing
- Evaluate API behavior under high concurrency.
- Confirm adherence to any rate limiting rules.

### 3.15 Usability Testing
- Assess API usability from a developer perspective.

### 3.16 CI/CD and Monitoring
- Validate API behavior in CI/CD workflows.
- Recommend monitoring for performance and availability.

### 3.17 Backup and Recovery Testing
- Validate backup and recovery procedures for booking data.

### 3.18 Internationalization Testing
- Test support for different language inputs if applicable.

### 3.19 Third-Party Integration Testing
- Validate any external integrations impacting the API.

## 4. Test Environments
The test environments include:

- Windows 10: Chrome, Firefox, Edge
- macOS: Safari
- Android: Chrome
- iOS: Safari

### 4.1 Environment URLs
- QA: https://restful-booker.herokuapp.com/apidoc/index.html
- Pre-Prod: https://restful-booker.herokuapp.com/apidoc/index.html

### 4.2 Environment Setup
- Network: Wired, Wi-Fi, and mobile connectivity as available.
- Security: HTTPS access and authentication token management.
- Team roles: Testers, developers, and stakeholders with defined permissions.

## 5. Defect Reporting Procedure
Defects will be reported and managed through JIRA with the following process:

- Identify defects based on deviations from requirements, API behavior, or performance issues.
- Record reproduction steps, expected vs actual results, and attachments.
- Assign severity and priority.
- Triage issues and assign to the appropriate team member.
- Communicate defect status via daily updates and end-of-day summaries.

### 5.1 Points of Contact
- Frontend: Devesh
- Backend: Sonal
- DevOps: Prajeeth

## 6. Test Strategy
Testing will follow a structured approach:

1. Create test scenarios and test cases for all scope items.
2. Use test design techniques including:
   - Equivalence class partitioning
   - Boundary value analysis
   - Decision table testing
   - State transition testing
   - Use case testing
3. Apply exploratory testing and error guessing.
4. Execute smoke tests first and reject build if smoke fails.
5. Perform in-depth testing after a stable build is available.
6. Run multiple testers across supported environments in parallel.
7. Report defects and progress daily.

### 6.1 Testing Types
- Smoke and sanity testing
- Regression and retesting
- Functional testing
- Usability testing
- Exploratory testing
- End-to-end workflow testing

### 6.2 Best Practices
- Context-driven testing
- Shift-left testing
- Exploratory testing
- End-to-end flow coverage

## 7. Test Schedule
A high-level schedule is planned as follows:

- Test plan creation
- Test case creation
- Test case execution
- Summary report delivery

Planned duration: 2 sprints

## 8. Test Deliverables
### 8.1 Deliverables
- Test Plan: scope, strategy, schedule, resources, and deliverables.
- Functional Test Cases: test cases for the defined scope.
- Defect Reports: detailed defects with reproduction steps and evidence.
- Summary Reports: bug metrics and status summaries.

## 9. Entry and Exit Criteria
### 9.1 Requirement Analysis
Entry Criteria:
- Requirement documents or project details available.
Exit Criteria:
- Requirements understood and clarified.

### 9.2 Test Execution
Entry Criteria:
- Test scenarios and cases signed off.
- Application ready for testing.
Exit Criteria:
- Test case execution reports and defect reports completed.

### 9.3 Test Closure
Entry Criteria:
- Test execution and defect reporting completed.
Exit Criteria:
- Test summary reports completed.

## 10. Tools
Tools planned for use:
- JIRA for defect tracking
- Mind map tools for test planning
- Screenshot/snipping tools
- Word and Excel for documentation and reporting

## 11. Risks and Mitigations
- Risk: Resource unavailability
  - Mitigation: Backup resource planning
- Risk: Build URL unavailable
  - Mitigation: Switch to alternate tasks
- Risk: Limited testing time
  - Mitigation: Scale resources dynamically

## 12. Approvals
Testing artifacts requiring approval:
- Test Plan
- Test Scenarios
- Test Cases
- Reports

> Testing proceeds to the next phase only after required approvals are obtained.
