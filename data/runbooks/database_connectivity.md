# Database Connectivity Runbook

## Symptoms
- Application timeouts
- Failed transactions
- Database connection errors
- Increased retry volume from dependent services

## Initial Checks
1. Verify database instance health
2. Review connection counts and pool saturation
3. Check recent schema or network changes
4. Validate application secrets and credentials
5. Review latency between application and database tiers

## Common Causes
- Connection pool exhaustion
- Expired or rotated credentials
- Database resource saturation
- Network path degradation
- Schema lock contention

## Immediate Actions
- Confirm whether the issue affects one service or multiple services
- Check whether failover occurred
- Recycle application connections only if safe and approved
- Escalate to the database owner if availability or integrity is at risk
