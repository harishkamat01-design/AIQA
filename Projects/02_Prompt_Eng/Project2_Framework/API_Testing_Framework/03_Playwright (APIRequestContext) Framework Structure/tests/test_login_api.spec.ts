import { test, expect, request } from '@playwright/test';
import { config } from '../utils/config';
import { getPayload } from '../utils/dataLoader';
import { validateSchema } from '../utils/schemaValidator';

const payload = getPayload('login');

test('verify login API returns valid token', async () => {
  const apiContext = await request.newContext({ baseURL: config.baseUrl });
  const response = await apiContext.post(config.endpoints.auth, {
    data: payload,
    headers: { 'Content-Type': 'application/json' }
  });

  expect(response.status()).toBe(200);
  const responseBody = await response.json();
  expect(responseBody.token).toBeTruthy();
  validateSchema(responseBody, 'login_schema.json');
});
