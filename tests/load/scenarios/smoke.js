import http from 'k6/http';
import { check, sleep } from 'k6';
import { BASE_URL } from '../config.js';

export function runSmokeScenarios() {
  // LOAD-001 to LOAD-040 smoke validations
  const resRoot = http.get(`${BASE_URL}/`);
  check(resRoot, {
    'LOAD-001 Root 200': (r) => r.status === 200,
  });

  const resHealth = http.get(`${BASE_URL}/health`);
  check(resHealth, {
    'LOAD-002 Health 200': (r) => r.status === 200,
  });

  const resStats = http.get(`${BASE_URL}/api/v1/stats`);
  check(resStats, {
    'LOAD-003 Stats 200': (r) => r.status === 200,
  });

  const resGenes = http.get(`${BASE_URL}/api/v1/genes?limit=20`);
  check(resGenes, {
    'LOAD-004 Genes 200': (r) => r.status === 200,
  });

  const resDiseases = http.get(`${BASE_URL}/api/v1/diseases?limit=20`);
  check(resDiseases, {
    'LOAD-006 Diseases 200': (r) => r.status === 200,
  });

  const resVariants = http.get(`${BASE_URL}/api/v1/variants?limit=20`);
  check(resVariants, {
    'LOAD-008 Variants 200': (r) => r.status === 200,
  });

  const resPathways = http.get(`${BASE_URL}/api/v1/pathways?limit=20`);
  check(resPathways, {
    'LOAD-009 Pathways 200': (r) => r.status === 200,
  });

  const resAssoc = http.get(`${BASE_URL}/api/v1/associations?limit=20`);
  check(resAssoc, {
    'LOAD-010 Associations 200': (r) => r.status === 200,
  });

  const resSearch = http.get(`${BASE_URL}/api/v1/search?q=BRCA1`);
  check(resSearch, {
    'LOAD-014 Search 200': (r) => r.status === 200,
  });

  sleep(0.5);
}
