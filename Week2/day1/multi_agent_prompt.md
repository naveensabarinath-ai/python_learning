# Multi-Agent Prompting

Multi-agent prompting means dividing a complex problem among multiple specialized AI agents. Each agent has a distinct responsibility, and an orchestrator coordinates how their outputs flow together.

## Simple use case: developing a new IT feature

### Feature request
"Add Employee Leave Balance Notification"

When an employee’s leave balance falls below 2 days, the system should notify the employee.

### Multi-agent workflow

```text
User Requirement
       │
       ▼
Orchestrator Agent
       │
   ┌───┼───────────────┐
   ▼   ▼               ▼
Requirements   Architecture   Security
Agent          Agent          Agent
   │   │               │
   └───┼───────────────┘
       ▼
Development Agent
       │
       ▼
Test Agent
       │
       ▼
Review Agent
       │
       ▼
Final Solution
```

## Sample multi-agent prompt

```text
You are an AI software development team consisting of multiple specialized agents.

Your goal is to design and implement the following feature:

FEATURE:
"Employee Leave Balance Notification"

REQUIREMENT:
When an employee's available leave balance falls below 2 days, the system should automatically send a notification to the employee.

Create and coordinate the following agents.

AGENT 1 — REQUIREMENTS ANALYST
Responsibilities:
- Understand the business requirement.
- Identify functional requirements.
- Identify non-functional requirements.
- Identify edge cases.
- Create acceptance criteria.

Output:
Requirements Specification.

---

AGENT 2 — SOLUTION ARCHITECT
Responsibilities:
- Design the technical solution.
- Identify affected services or components.
- Design API changes.
- Design database changes.
- Identify integration requirements.
- Consider scalability and reliability.

Input:
Requirements Specification from Agent 1.

Output:
Technical Design.

---

AGENT 3 — SECURITY ENGINEER
Responsibilities:
- Review the proposed design for security risks.
- Identify authentication and authorization requirements.
- Check sensitive data handling.
- Identify potential vulnerabilities.
- Recommend security controls.

Input:
Requirements Specification + Technical Design.

Output:
Security Review.

---

AGENT 4 — DEVELOPER
Responsibilities:
- Convert the approved technical design into implementation tasks.
- Define classes, modules, or services to modify.
- Provide pseudocode or implementation guidance.
- Identify dependencies.
- Follow coding best practices.

Input:
Requirements + Technical Design + Security Review.

Output:
Implementation Plan.

---

AGENT 5 — TEST ENGINEER
Responsibilities:
- Create test scenarios.
- Create positive and negative test cases.
- Create API test cases.
- Create integration test cases.
- Identify edge cases.
- Define automation opportunities.

Input:
Requirements + Technical Design + Implementation Plan.

Output:
Test Plan.

---

AGENT 6 — REVIEW AGENT
Responsibilities:
- Review all outputs from the previous agents.
- Identify inconsistencies.
- Check whether all requirements are covered.
- Identify missing security, testing, or implementation considerations.
- Recommend corrections.

Output:
Final Review.

---

ORCHESTRATOR AGENT
You are responsible for coordinating all agents.

Rules:
1. Start with the Requirements Analyst.
2. Pass its output to the Solution Architect.
3. Pass the architecture to the Security Engineer.
4. Pass the approved design to the Developer.
5. Pass the implementation plan to the Test Engineer.
6. Send all outputs to the Review Agent.
7. If the Review Agent identifies major issues, send the relevant work back to the appropriate agent for revision.
8. Do not proceed to the next stage if a critical requirement is missing.
9. Maintain traceability between requirements, design, implementation, and testing.

Final output must contain:
1. Business Requirements
2. Acceptance Criteria
3. Technical Architecture
4. Security Considerations
5. Implementation Plan
6. Test Plan
7. Review Findings
8. Final Recommendation

Clearly identify which agent produced each section.
```

## Example flow

```text
User Requirement
       │
       ▼
Requirements Agent
       │
       │ "Notification required when balance < 2 days"
       ▼
Architecture Agent
       │
       │ "Add Leave Balance Monitor + Notification Service"
       ▼
Security Agent
       │
       │ "Validate employee identity and notification permissions"
       ▼
Developer Agent
       │
       │ "Implement balance check + notification trigger"
       ▼
Test Agent
       │
       │ "Test balances of 0, 1, 2, and 3 days; include failure cases"
       ▼
Review Agent
       │
       │ "All requirements covered"
       ▼
Final Solution
```

## Why multi-agent prompting?

The main advantage is specialization.

A single AI might need to think about requirements, architecture, security, coding, and testing all at once. With multiple agents:

Requirements Agent → Architecture Agent → Security Agent → Developer Agent → Test Agent → Review Agent

Each agent focuses on one responsibility, while the orchestrator manages the workflow and keeps the process consistent.

## Multi-agent vs. ToT vs. ReAct

| Technique | Core idea | Example |
|---|---|---|
| Chain of Thought | One reasoning path | Solve a technical problem step by step |
| Tree of Thought | Multiple reasoning paths | Compare three architecture options |
| ReAct | Reason + Act + Observe | Investigate a production issue |
| Multi-Agent | Multiple specialized agents | Requirements → Architecture → Development → Testing |

This makes multi-agent prompting especially useful for large software tasks where different expert perspectives are required before final implementation.