# Test Plan

## 1. Document Control
- Document Title: VWO Login and Dashboard Test Plan
- Document Owner: QA Team
- Version: 1.0
- Date: [PLACEHOLDER]
- Status: Draft

## 2. Purpose
This test plan defines the QA approach for verifying the VWO application login workflow and dashboard access. It validates authentication, error handling, dashboard navigation, and supporting quality attributes.

## 3. Background
The application under test is the VWO login page at https://app.vwo.com/. The main user flow begins with a login page and, upon successful authentication, transitions to a dashboard page. Invalid login attempts must be handled with a visible error page or error message.

## 4. Scope
### In Scope
- Login page rendering and field validation
- Valid login workflow
- Invalid login workflow
- Dashboard access after successful login
- Error handling for invalid credentials

### Out of Scope
- Account registration
- Password recovery
- Full dashboard feature functionality beyond access/navigation validation
- External integrations not described in the PRD

## 5. Objectives
- Verify the login page loads and is functional.
- Verify a valid login navigates to the dashboard.
- Verify invalid credentials trigger an error page or message.
- Verify the dashboard button is visible and usable after login.
- Validate end-to-end login-to-dashboard flow.

## 6. Test Strategy
### Test Types
- Functional Testing
- Regression Testing
- Positive and Negative Testing
- UI Validation
- Accessibility Testing
- Security Testing
- Performance/Response Testing

### Approach
- Use exploratory validation for the login and dashboard workflow.
- Use automated Playwright-style scripts for repeatable coverage.
- Execute tests in isolated browser sessions.
- Capture defects for any failed login, navigation, or error handling behavior.

## 7. Features to be Tested
- Login page fields and submission
- Successful authentication path
- Invalid login error handling
- Dashboard button and dashboard page access
- Page transitions and URL validation

## 8. Acceptance Criteria
- AC-001: Login page displays username/email and password input fields.
- AC-002: Valid credentials navigate to the dashboard page.
- AC-003: Invalid credentials display an error page or clear error message.
- AC-004: Dashboard button is visible after successful login.
- AC-005: The dashboard is not accessible without successful authentication.

## 9. Test Environment
- Browser: [PLACEHOLDER: Chrome/Firefox/Edge/Safari]
- URL: https://app.vwo.com/
- Network: Stable internet connection
- Test data: Valid login credentials, invalid login credentials

## 10. Test Data
- Valid login credentials: [PLACEHOLDER]
- Invalid password credentials: [PLACEHOLDER]
- Invalid username credentials: [PLACEHOLDER]
- Empty username/password combinations

## 11. Deliverables
- test plan.md
- test_cases.csv
- playwright_test_cases.md
- test_cases.md
- Test execution results
- Defect reports for failed scenarios

## 12. Risks and Mitigation
- Risk: Invalid or expired test account credentials.
  - Mitigation: Verify credentials before automation execution.
- Risk: UI changes on VWO login or dashboard pages.
  - Mitigation: Use resilient selectors and update tests accordingly.
- Risk: Network instability causing false failures.
  - Mitigation: Execute tests on a stable connection and retry if infrastructure issues occur.

## 13. Entry Criteria
- PRD is available and reviewed.
- Test environment is configured.
- Login page is accessible.
- Valid and invalid credential sets are defined.

## 14. Exit Criteria
- All planned login and dashboard tests are executed.
- All critical defects are logged.
- Test results are reviewed.
- Known open issues are documented.
