export const THRESHOLDS = {
  smoke: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<300']
  },
  load: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  },
  stress: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<1000']
  },
  spike: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<1500']
  },
  soak: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  },
  api: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<400']
  },
  auth: {
    http_req_failed: ['rate<0.02'],
    http_req_duration: ['p(95)<450']
  }
};
