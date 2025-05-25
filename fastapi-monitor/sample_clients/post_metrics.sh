#!/bin/bash
# filepath: ./run_metrics.sh

# Usage: ./run_metrics.sh [N]
# N = interval in minutes (default: 5)

INTERVAL_MINUTES=${1:-5}

while true; do
  curl -X POST "http://localhost:8000/api/metrics/?cpu=58.2&memory=14"
  sleep $((INTERVAL_MINUTES * 60))
done