---
name: launchdarkly
description: Manages LaunchDarkly feature flags, targeting rules, and rollouts. Creates flags for A/B tests, manages gradual rollouts, and integrates with ab-test-designer skill.
---

# LaunchDarkly — Feature Flags & Experimentation

## Purpose
Manage feature flags and gradual rollouts as part of the product discovery-to-delivery pipeline. Directly complements the `ab-test-designer` skill by implementing experiment configurations as feature flags.

## Integration Options
1. **MCP Server** (recommended): Official `@launchdarkly/mcp-server` — configured in `.claude/.mcp.json`
2. **CLI**: `ldcli` for scripting and CI/CD operations
3. **REST API**: Full management API at `https://app.launchdarkly.com/api/v2`
4. **Python SDK**: `launchdarkly-api` for custom scripts

## Capabilities via MCP
- Create and manage feature flags
- Configure targeting rules (user segments, percentages)
- Set up gradual rollouts
- Manage AI configs
- Toggle flags across environments

## CLI Reference (ldcli)

### Authentication
```bash
ldcli login                              # Interactive browser login
ldcli config --set access-token TOKEN    # Token-based auth
```

### Flag Management
```bash
ldcli flags list --project PROJECT_KEY
ldcli flags create --project PROJECT_KEY --name "New Feature" --key new-feature
ldcli flags toggle --project PROJECT_KEY --environment production --flag new-feature
ldcli flags targeting --project PROJECT_KEY --environment staging --flag new-feature
```

### Local Development
```bash
ldcli dev-server                         # Run local flag evaluation server
```

## Workflows

### From A/B Test Design → Feature Flag
When `ab-test-designer` produces experiment plans:
1. Read experiment from `/2-solution/2e-roadmap/ab-tests/experiment-*.md`
2. Create feature flag with experiment key: `exp_{experiment_slug}`
3. Configure variants (control + treatment)
4. Set targeting rules (audience segment, allocation %)
5. Set guardrail metric alerts

### Gradual Rollout
For MVP features going to production:
1. Create flag for each MVP feature
2. Configure rollout schedule:
   - 5% → internal team (canary)
   - 25% → beta users
   - 50% → half users
   - 100% → general availability
3. Monitor guardrail metrics between each stage

### Kill Switch
For any launched feature:
- Quick toggle to disable without deploy
- Pre-configured for all experiment flags

### Environment Management
```
Environments: development → staging → production
Flags sync: Create in dev, promote to staging, then production
```

## PM Query Patterns
- "Create a feature flag for the new onboarding flow"
- "Set up a 50/50 split for experiment X"
- "Roll out feature Y to 25% of users in production"
- "Kill the experiment Z flag immediately"
- "Show me all active experiments in production"
- "List flags that haven't been cleaned up (stale > 30 days)"

## Output Integration
- Flag configurations logged in `/2-solution/2e-roadmap/ab-tests/`
- Cross-reference: `[Flag: flag-key-name]`
- Experiment results inform next discovery cycle

## Rules
- ALWAYS create flags in development environment first
- NEVER toggle production flags without confirmation
- Tag experiment flags with `experiment` tag
- Include rollback plan for every flag
- Clean up flags after experiments conclude
- Mark AI-created flags with `ai-managed` tag
