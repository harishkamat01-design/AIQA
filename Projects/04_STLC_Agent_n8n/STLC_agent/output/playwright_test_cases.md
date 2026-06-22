# Playwright Test Cases

## Page Objects

### `pages/login.page.ts`
```typescript
import { Page, Locator, expect } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly usernameInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.getByLabel('Email') || page.getByPlaceholder('Email');
    this.passwordInput = page.getByLabel('Password') || page.getByPlaceholder('Password');
    this.loginButton = page.getByRole('button', { name: /log ?in/i });
    this.errorMessage = page.getByRole('alert');
  }

  async goto(): Promise<void> {
    await this.page.goto('https://app.vwo.com/');
  }

  async login(username: string, password: string): Promise<void> {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async expectError(text: RegExp | string): Promise<void> {
    await expect(this.errorMessage).toBeVisible();
    await expect(this.errorMessage).toContainText(text);
  }
}
```

### `pages/dashboard.page.ts`
```typescript
import { Page, Locator, expect } from '@playwright/test';

export class DashboardPage {
  readonly page: Page;
  readonly dashboardHeading: Locator;
  readonly dashboardButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.dashboardHeading = page.getByRole('heading', { name: /dashboard/i });
    this.dashboardButton = page.getByRole('button', { name: /dashboard/i });
  }

  async expectVisible(): Promise<void> {
    await expect(this.dashboardHeading).toBeVisible();
    await expect(this.dashboardButton).toBeVisible();
  }
}
```

## Spec: `tests/e2e/auth/login.spec.ts`
```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../../pages/login.page';
import { DashboardPage } from '../../pages/dashboard.page';

const validUser = process.env.VWO_VALID_USER || 'valid@example.com';
const validPassword = process.env.VWO_VALID_PASSWORD || 'ValidPassword123!';

test.describe('VWO login flow', () => {
  let loginPage: LoginPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.goto();
  });

  test('should login with valid credentials and reach dashboard', async ({ page }) => {
    await loginPage.login(validUser, validPassword);
    const dashboardPage = new DashboardPage(page);
    await dashboardPage.expectVisible();
    await expect(page).toHaveURL(/dashboard|home/i);
  });

  test('should show error for invalid password', async () => {
    await loginPage.login(validUser, 'WrongPassword123!');
    await loginPage.expectError(/invalid|incorrect/i);
  });

  test('should show error for invalid username', async () => {
    await loginPage.login('invalid@example.com', validPassword);
    await loginPage.expectError(/invalid|incorrect/i);
  });

  test('should show validation message for empty credentials', async () => {
    await loginPage.login('', '');
    await loginPage.expectError(/required|cannot be empty/i);
  });
});
```

## Spec: `tests/e2e/dashboard/dashboard.spec.ts`
```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../../pages/login.page';
import { DashboardPage } from '../../pages/dashboard.page';

const validUser = process.env.VWO_VALID_USER || 'valid@example.com';
const validPassword = process.env.VWO_VALID_PASSWORD || 'ValidPassword123!';

test.describe('VWO dashboard access', () => {
  test('should display dashboard button after successful login', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login(validUser, validPassword);

    const dashboardPage = new DashboardPage(page);
    await dashboardPage.expectVisible();
  });

  test('should prevent dashboard access with invalid login', async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('invalid@example.com', 'WrongPassword123!');
    await loginPage.expectError(/invalid|incorrect/i);
    await expect(page).not.toHaveURL(/dashboard|home/i);
  });
});
```

## Notes
- Use environment variables for valid credentials.
- Adjust selectors if the live login page uses different labels or placeholder text.
- This file provides Playwright markdown-ready scripts for login and dashboard validation.
