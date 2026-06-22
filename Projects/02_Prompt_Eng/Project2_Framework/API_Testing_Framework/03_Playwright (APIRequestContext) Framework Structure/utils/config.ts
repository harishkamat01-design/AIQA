import fs from 'fs';
import path from 'path';

const configPath = path.resolve(__dirname, '../config/config.json');

type Endpoints = {
  auth: string;
  booking: string;
  bookingList: string;
};

export type Config = {
  baseUrl: string;
  endpoints: Endpoints;
};

export const config: Config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
