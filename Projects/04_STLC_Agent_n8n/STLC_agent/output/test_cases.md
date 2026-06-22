# Test Cases Overview

## Spec Files
- `tests/e2e/auth/login.spec.ts`
- `tests/e2e/dashboard/dashboard.spec.ts`

## Test Case Summary
The following test cases are derived from the test plan and cover valid and invalid login scenarios plus dashboard access verification.

### Login Test Cases
- TC-001: Valid login navigates to dashboard
- TC-002: Invalid password shows error
- TC-003: Invalid username shows error
- TC-004: Empty credentials show validation

### Dashboard Test Cases
- TC-005: Dashboard button visible after login
- TC-006: Invalid login prevents dashboard access
- TC-007: Error page displays invalid login message
- TC-008: Dashboard content loads after login

## Test Case Details
1. **TC-001** — Valid login navigates to dashboard
   - Description: Verify valid credentials navigate the user from the login page to the dashboard.

2. **TC-002** — Invalid password shows error
   - Description: Verify a valid username with an invalid password displays an error page or message.

3. **TC-003** — Invalid username shows error
   - Description: Verify an invalid username with a valid password displays an error page or message.

4. **TC-004** — Empty credentials show validation
   - Description: Verify submitting blank username and password fields produces validation feedback.

5. **TC-005** — Dashboard button visible after login
   - Description: Verify the dashboard button is visible and accessible after successful login.

6. **TC-006** — Invalid login prevents dashboard access
   - Description: Verify invalid login does not allow access to the dashboard.

7. **TC-007** — Error page displays invalid login message
   - Description: Verify the invalid login error page or message clearly indicates bad credentials.

8. **TC-008** — Dashboard content loads after login
   - Description: Verify core dashboard content or heading loads after successful authentication.

## Automation Mapping
- `tests/e2e/auth/login.spec.ts`: Implements TC-001 through TC-004.
- `tests/e2e/dashboard/dashboard.spec.ts`: Implements TC-005 through TC-008.

## Notes
- The test plan focuses on the login and dashboard workflow for https://app.vwo.com/.
- Valid and invalid login coverage is included.
- Dashboard access validation is included after successful login.
