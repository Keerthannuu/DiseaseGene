export const BASE_URL = __ENV.LOAD_TEST_BASE_URL || 'http://localhost:8000';
export const PROFILE = __ENV.LOAD_TEST_PROFILE || 'smoke';
export const VUS = parseInt(__ENV.LOAD_TEST_VUS || '10', 10);
export const DURATION = __ENV.LOAD_TEST_DURATION || '30s';

export const TEST_USERS = {
  researcher: {
    username: __ENV.TEST_USERNAME || 'test_researcher',
    password: __ENV.TEST_PASSWORD || 'TestPassword123!'
  },
  admin: {
    username: __ENV.ADMIN_USERNAME || 'test_admin',
    password: __ENV.ADMIN_PASSWORD || 'AdminPassword123!'
  }
};
