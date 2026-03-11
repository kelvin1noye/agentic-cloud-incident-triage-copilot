# Deployment Rollback Runbook

## Triggers for Rollback
- Incident begins immediately after deployment
- Error rates materially increase after release
- New version causes instability or service degradation
- User-facing impact exceeds acceptable thresholds

## Validation Checks
1. Confirm deployment timestamp and scope
2. Review release notes and changed components
3. Compare metrics before and after deployment
4. Verify whether rollback prerequisites are met
5. Confirm stakeholder communication path

## Rollback Considerations
- Check for database schema compatibility
- Confirm rollback does not worsen downstream dependencies
- Ensure support teams are informed before execution
- Validate post-rollback service health

## Escalation Guidance
- Notify incident commander or team lead
- Coordinate with application owner
- Escalate to release management if rollback affects multiple services
