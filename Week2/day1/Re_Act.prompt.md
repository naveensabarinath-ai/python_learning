# ReAct Prompting

ReAct = Reason + Act

ReAct prompting is useful when an AI system needs to:

- reason about a problem,
- take a relevant action or tool step,
- observe the result,
- decide the next action based on evidence.

This is especially useful for debugging, troubleshooting, and investigation workflows.

## Simple use case: IT production incident

### Scenario
A production API is returning HTTP 500 errors. An AI assistant needs to investigate the issue.

### ReAct flow
```text
Problem
   ↓
Reason about what to check
   ↓
Act → Check application logs
   ↓
Observe the result
   ↓
Reason about the next step
   ↓
Act → Check database
   ↓
Observe the result
   ↓
Reason about the next step
   ↓
Act → Check recent deployment
   ↓
Final diagnosis
   ↓
Recommended fix
```

## Sample prompt

```text
You are an experienced DevOps and Production Support Engineer.

A production REST API has started returning HTTP 500 errors.

Incident details:
- Application: Employee Leave Management API
- Error rate: 35%
- Started: 15 minutes ago
- Users are unable to submit leave requests
- No known infrastructure outage

Use a ReAct-style approach to investigate the incident.

For each step:
1. Reason about what information is needed.
2. Select the most appropriate action/tool.
3. Analyze the observation or result.
4. Decide the next action based on the result.
5. Continue until the root cause is identified.

Available actions:
- CHECK_LOGS
- CHECK_DATABASE
- CHECK_API_HEALTH
- CHECK_RECENT_DEPLOYMENTS
- CHECK_INFRASTRUCTURE
- CHECK_EXTERNAL_DEPENDENCIES

Investigation rules:
- Do not assume the root cause.
- Start with the highest-value diagnostic check.
- Use each result to determine the next action.
- Avoid unnecessary checks.
- Clearly distinguish facts from assumptions.
- Stop when there is sufficient evidence for a root-cause diagnosis.

At the end, provide:
1. Root cause
2. Evidence supporting the diagnosis
3. Immediate remediation
4. Long-term preventive action
5. Recommended monitoring or alerting

Use this format:

Thought: What needs to be investigated?
Action: <action>
Observation: <result>
Next Step: What should be investigated next?

Repeat the cycle until the investigation is complete.
```

## Example execution

```text
Thought:
The API is returning 500 errors, so I should first determine whether the application itself is unhealthy.

Action:
CHECK_API_HEALTH

Observation:
The API is reachable, but the Leave Submission endpoint is returning 500.

Next Step:
Check application logs to identify the actual exception.

Action:
CHECK_LOGS

Observation:
Logs show "Database connection pool exhausted."

Next Step:
Check whether the database is experiencing high load or connection issues.

Action:
CHECK_DATABASE

Observation:
The database is healthy, but 200+ connections are active. Normal usage is approximately 40 connections.

Next Step:
Check recent deployments for a possible connection leak.

Action:
CHECK_RECENT_DEPLOYMENTS

Observation:
A new release was deployed 20 minutes ago. The release introduced a database connection that is not being closed.

Conclusion:
The recent deployment caused a database connection leak, which exhausted the connection pool and caused HTTP 500 errors.
```

## Why ReAct is useful

ReAct helps the AI behave more like a real investigator:

- it reasons before acting,
- it uses tool results to guide the next move,
- it avoids guessing,
- it reaches a diagnosis with evidence instead of assumptions.

This makes it especially helpful for troubleshooting, root-cause analysis, and decision-based engineering tasks.