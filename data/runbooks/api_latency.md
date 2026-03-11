# API Latency Runbook

## Symptoms
- Increased response times
- Elevated 5xx rates
- Timeouts from dependent services
- User complaints about slow transactions

## Initial Checks
1. Review recent deployments and configuration changes
2. Check CPU and memory utilization
3. Inspect database latency and connection usage
4. Review upstream and downstream service health
5. Confirm autoscaling activity and pod/container health

## Common Causes
- Recent faulty deployment
- Database connection pool exhaustion
- External dependency slowdown
- Traffic spike without sufficient scaling
- Misconfigured cache or expired cache warmup behavior

## Immediate Actions
- Roll back the most recent deployment if the timing strongly correlates
- Scale horizontally if saturation is confirmed
- Restart degraded workloads only if it is approved and low risk
- Escalate to the application owner if customer impact is growing
