import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL, TEST_USERS } from '../config.js';

export function runLoadScenarios() {
  // LOAD-041 to LOAD-100: Normal Load
  const params = { headers: { 'Accept': 'application/json' } };
  
  // 1. Browsing genes with pagination
  const r1 = http.get(`${BASE_URL}/api/v1/genes?skip=0&limit=50`, params);
  check(r1, { 'Load Genes 200': (r) => r.status === 200 });

  // 2. Filtered genes
  const r2 = http.get(`${BASE_URL}/api/v1/genes?chromosome=17`, params);
  check(r2, { 'Load Genes Chr17 200': (r) => r.status === 200 });

  // 3. Diseases
  const r3 = http.get(`${BASE_URL}/api/v1/diseases?skip=0&limit=50`, params);
  check(r3, { 'Load Diseases 200': (r) => r.status === 200 });

  // 4. Search
  const r4 = http.get(`${BASE_URL}/api/v1/search?q=TP53`, params);
  check(r4, { 'Load Search 200': (r) => r.status === 200 });

  sleep(1);
}

export function runStressScenarios() {
  // LOAD-101 to LOAD-160: Stress Load
  const endpoints = [
    '/api/v1/stats',
    '/api/v1/genes?limit=100',
    '/api/v1/diseases?limit=100',
    '/api/v1/search?q=BRCA&type=gene',
    '/api/v1/associations?limit=50'
  ];
  const url = `${BASE_URL}${endpoints[Math.floor(Math.random() * endpoints.length)]}`;
  const res = http.get(url);
  check(res, { 'Stress Query Success': (r) => r.status === 200 || r.status === 304 });
  sleep(0.2);
}

export function runSpikeScenarios() {
  // LOAD-161 to LOAD-200: Sudden Spike
  const res = http.get(`${BASE_URL}/api/v1/search?q=cancer`);
  check(res, { 'Spike Query Handled': (r) => r.status === 200 || r.status === 429 });
}

export function runSoakScenarios() {
  // LOAD-201 to LOAD-240: Endurance
  const res = http.get(`${BASE_URL}/api/v1/stats`);
  check(res, { 'Soak Stats Healthy': (r) => r.status === 200 });
  sleep(2);
}

export function runApiPerformanceScenarios() {
  // LOAD-241 to LOAD-275: DB-Heavy
  const resStats = http.get(`${BASE_URL}/api/v1/stats`);
  check(resStats, { 'DB Stats Aggregation 200': (r) => r.status === 200 });

  const resDeep = http.get(`${BASE_URL}/api/v1/genes?skip=500&limit=100`);
  check(resDeep, { 'Deep Pagination 200': (r) => r.status === 200 });
  sleep(1);
}

export function runAuthScenarios() {
  // LOAD-276 to LOAD-300: Auth load
  const payload = `username=${encodeURIComponent(TEST_USERS.researcher.username)}&password=${encodeURIComponent(TEST_USERS.researcher.password)}`;
  const headers = { 'Content-Type': 'application/x-www-form-urlencoded' };
  
  const res = http.post(`${BASE_URL}/api/v1/auth/login`, payload, { headers: headers });
  check(res, { 'Auth Login Handled': (r) => r.status === 200 || r.status === 401 });
  sleep(1);
}
