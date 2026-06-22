import { test, expect, request } from '@playwright/test';
import { config } from '../utils/config';


test('verify booking list API returns a list', async () => {
  const apiContext = await request.newContext({ baseURL: config.baseUrl });
  const response = await apiContext.get(config.endpoints.bookingList, {
    headers: { 'Accept': 'application/json' }
  });

  expect(response.status()).toBe(200);
  const responseBody = await response.json();
  expect(Array.isArray(responseBody)).toBeTruthy();
});
