import type { PlaywrightTestConfig } from '@playwright/test';

const config: PlaywrightTestConfig = {
  testDir: './tests',
  timeout: 30000,
  use: {
    baseURL: 'https://restful-booker.herokuapp.com',
    extraHTTPHeaders: {
      'Content-Type': 'application/json'
    }
  },
  reporter: [['list'], ['allure-playwright']]
};

export default config;
