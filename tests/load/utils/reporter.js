export function handleSummary(data) {
  const p50 = data.metrics.http_req_duration ? data.metrics.http_req_duration.values['p(50)'].toFixed(2) : '0';
  const p90 = data.metrics.http_req_duration ? data.metrics.http_req_duration.values['p(90)'].toFixed(2) : '0';
  const p95 = data.metrics.http_req_duration ? data.metrics.http_req_duration.values['p(95)'].toFixed(2) : '0';
  const p99 = data.metrics.http_req_duration ? data.metrics.http_req_duration.values['p(99)'].toFixed(2) : '0';
  const totalReqs = data.metrics.http_reqs ? data.metrics.http_reqs.values.count : 0;
  const errorRate = data.metrics.http_req_failed ? (data.metrics.http_req_failed.values.rate * 100).toFixed(2) : '0.00';

  const summaryObj = {
    profile: __ENV.LOAD_TEST_PROFILE || 'smoke',
    requests: totalReqs,
    error_rate_pct: parseFloat(errorRate),
    latency_ms: {
      p50: parseFloat(p50),
      p90: parseFloat(p90),
      p95: parseFloat(p95),
      p99: parseFloat(p99)
    },
    raw: data
  };

  return {
    'tests/load/reports/summary.json': JSON.stringify(summaryObj, null, 2),
    stdout: `
=====================================
K6 LOAD TEST SUMMARY
=====================================
Profile: ${__ENV.LOAD_TEST_PROFILE || 'smoke'}
Requests: ${totalReqs}
Error Rate: ${errorRate}%

p50: ${p50}ms
p90: ${p90}ms
p95: ${p95}ms
p99: ${p99}ms

Reports saved to tests/load/reports/summary.json
=====================================
`
  };
}
