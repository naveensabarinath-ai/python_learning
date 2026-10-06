# Tree of Thought Prompt for Architecture Selection

You are a senior software architect.

We need to design an Employee Leave Management System for an organization.

## Requirements
- 10,000 employees
- Web application
- REST APIs
- Role-based access
- Integration with an existing HR system
- Expected high availability
- Easy to maintain

## Technology options
1. Java + Spring Boot
2. Python + FastAPI
3. Node.js + Express

## Task
Use a Tree of Thought approach to evaluate the options before recommending a final architecture.

### Step 1: Generate three independent solution branches
- Branch A: Java + Spring Boot
- Branch B: Python + FastAPI
- Branch C: Node.js + Express

### Step 2: Evaluate each branch on the following criteria
- Performance
- Scalability
- Security
- Maintainability
- Development speed
- Integration capability
- Team skill requirements
- Long-term support

### Step 3: Identify strengths and weaknesses
For each branch, list:
- advantages
- limitations
- trade-offs

### Step 4: Score each option
Assign a score from 1 to 10 for each evaluation criterion.

### Step 5: Compare and eliminate weaker options
- Compare the branches objectively
- Eliminate options that are weaker based on evidence
- Explain the reasoning behind each elimination

### Step 6: Select the best architecture
Choose the best solution and explain why it is stronger than the alternatives.

### Step 7: Final recommendation
Provide:
- Recommended technology
- High-level architecture
- Key components
- Risks
- Mitigation strategies

Do not choose the first reasonable option. Explore and compare multiple alternatives before making the final recommendation.

## Expected flow

```text
                    Problem
                       │
          ┌────────────┼────────────┐
          │            │            │
       Branch A     Branch B     Branch C
      Java/Spring   Python      Node.js
          │            │            │
       Evaluate     Evaluate     Evaluate
          │            │            │
          └────────────┼────────────┘
                       │
                  Compare
                       │
                 Eliminate weak
                   options
                       │
                       ▼
              Best Solution
```

## Goal
The final answer should be a well-supported architecture decision, not a guess. Use structured reasoning, compare trade-offs, and justify the selected technology with practical business and engineering considerations.