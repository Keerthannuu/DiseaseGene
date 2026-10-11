import { PROFILE, VUS, DURATION } from './config.js';
import { THRESHOLDS } from './utils/thresholds.js';
import { handleSummary as customHandleSummary } from './utils/reporter.js';
import { runSmokeScenarios } from './scenarios/smoke.js';
import {
  runLoadScenarios,
  runStressScenarios,
  runSpikeScenarios,
  runSoakScenarios,
  runApiPerformanceScenarios,
  runAuthScenarios
} from './scenarios/scenarios_bundle.js';

function getStages(profile) {
  switch (profile) {
    case 'smoke':
      return [
        { duration: '5s', target: 2 },
        { duration: '10s', target: 2 },
        { duration: '5s', target: 0 }
      ];
    case 'load':
      return [
        { duration: '30s', target: 20 },
        { duration: '1m', target: 30 },
        { duration: '30s', target: 0 }
      ];
    case 'stress':
      return [
        { duration: '30s', target: 50 },
        { duration: '1m', target: 100 },
        { duration: '30s', target: 200 },
        { duration: '30s', target: 0 }
      ];
    case 'spike':
      return [
        { duration: '10s', target: 10 },
        { duration: '15s', target: 250 },
        { duration: '30s', target: 250 },
        { duration: '15s', target: 10 }
      ];
    case 'soak':
      return [
        { duration: '1m', target: 20 },
        { duration: '5m', target: 20 },
        { duration: '30s', target: 0 }
      ];
    case 'api':
      return [
        { duration: '15s', target: 15 },
        { duration: '30s', target: 25 },
        { duration: '15s', target: 0 }
      ];
    case 'authentication':
      return [
        { duration: '10s', target: 10 },
        { duration: '20s', target: 20 },
        { duration: '10s', target: 0 }
      ];
    default:
      return [
        { duration: '10s', target: 5 },
        { duration: '10s', target: 0 }
      ];
  }
}

export const options = {
  stages: getStages(PROFILE),
  thresholds: THRESHOLDS[PROFILE] || THRESHOLDS.smoke,
};

export default function () {
  switch (PROFILE) {
    case 'smoke':
      runSmokeScenarios();
      break;
    case 'load':
      runLoadScenarios();
      break;
    case 'stress':
      runStressScenarios();
      break;
    case 'spike':
      runSpikeScenarios();
      break;
    case 'soak':
      runSoakScenarios();
      break;
    case 'api':
      runApiPerformanceScenarios();
      break;
    case 'authentication':
      runAuthScenarios();
      break;
    default:
      runSmokeScenarios();
      break;
  }
}

export function handleSummary(data) {
  return customHandleSummary(data);
}
