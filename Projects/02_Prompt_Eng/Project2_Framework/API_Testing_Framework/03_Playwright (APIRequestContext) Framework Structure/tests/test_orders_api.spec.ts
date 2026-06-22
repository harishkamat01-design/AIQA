import { test, expect, request } from '@playwright/test';
import { config } from '../utils/config';
import { getPayload } from '../utils/dataLoader';

const bookingPayload = getPayload('booking');

test('verify create booking API returns bookingid', async () => {
  const apiContext = await request.newContext({ baseURL: config.baseUrl });
  const response = await apiContext.post(config.endpoints.booking, {
    data: bookingPayload,
    headers: { 'Content-Type': 'application/json' }
  });

  expect(response.status()).toBe(200);
  const responseBody = await response.json();
  expect(responseBody.bookingid).toBeGreaterThan(0);
});
