# Sequential Prompting in IT

## Simple example: adding a “Forgot Password” feature

Imagine a company wants this feature:

> Requirement: Users should be able to reset their password if they forget it.

Instead of giving the model everything in one prompt, we break the task into smaller, connected steps.

```text
Requirement
   ↓
Prompt 1 → User story
   ↓
Prompt 2 → Tasks
   ↓
Prompt 3 → Technical design
   ↓
Prompt 4 → Code
   ↓
Prompt 5 → Test cases
```

## Prompt 1: Requirement → User story

### Input
```text
Users should be able to reset their password if they forget it.
```

### Prompt
```text
You are a Product Owner.

Convert the following requirement into a user story.

Requirement:
<REQUIREMENT>

Provide:
1. User Story
2. Acceptance Criteria
3. Priority
```

### AI output
```text
User Story:
As a user,
I want to reset my password,
so that I can regain access to my account.

Acceptance Criteria:
1. User can select "Forgot Password".
2. User can enter their registered email.
3. System sends a reset link.
4. User can create a new password.
5. User can log in using the new password.

Priority: High
```

This output becomes the input for the next prompt.

## Prompt 2: User story → Tasks

### Input
```text
<OUTPUT_FROM_PROMPT_1>
```

### Prompt
```text
You are a Technical Lead.

Based on the following user story, create development tasks.

USER STORY:
<OUTPUT_FROM_PROMPT_1>

Create tasks for:
1. Frontend
2. Backend
3. Database
4. Security
5. Testing

Do not write code.
```

### AI output
```text
Frontend:
- Create Forgot Password page.
- Add email input.
- Add Reset Password page.

Backend:
- Create password reset API.
- Generate reset token.
- Validate reset token.
- Update password.

Database:
- Add reset token storage.

Security:
- Make reset token expire after a fixed period.
- Prevent token reuse.

Testing:
- Test valid reset request.
- Test invalid email.
- Test expired token.
- Test invalid token.
```

This becomes the input for the next prompt.

## Prompt 3: Tasks → Technical design

### Prompt
```text
You are a Software Architect.

Using the following user story and tasks, create a simple technical design.

USER STORY:
<OUTPUT_FROM_PROMPT_1>

TASKS:
<OUTPUT_FROM_PROMPT_2>

Technology:
- React
- Java Spring Boot
- PostgreSQL

Provide:
1. API design
2. Database design
3. Component flow
4. Security considerations

Do not write implementation code.
```

### AI output
```text
API:
POST /api/password/forgot

Request:
{
  "email": "user@example.com"
}

POST /api/password/reset

Request:
{
  "token": "...",
  "newPassword": "..."
}

Flow:
React
  ↓
Spring Boot API
  ↓
Password Service
  ↓
PostgreSQL
  ↓
Email Service
```

## Prompt 4: Technical design → Code

```text
You are a Senior Java Developer.

Implement the password reset API based ONLY on the approved technical design below.

TECHNICAL DESIGN:
<OUTPUT_FROM_PROMPT_3>

Requirements:
- Use Spring Boot.
- Follow the API design exactly.
- Implement input validation.
- Implement token validation.
- Handle errors properly.
- Do not change the approved architecture.

Provide:
1. Java code
2. Files created
3. Explanation
```

The AI generates the implementation code.

## Prompt 5: Code → Test cases

```text
You are a QA Engineer.

Create test cases for the following implementation.

TECHNICAL DESIGN:
<OUTPUT_FROM_PROMPT_3>

CODE:
<OUTPUT_FROM_PROMPT_4>

Cover:
1. Happy path
2. Invalid email
3. Invalid token
4. Expired token
5. Password validation failure
6. Successful password reset

Output:
Test ID
Scenario
Given
When
Then
Expected Result
```

### Example AI output
```text
TC-001
Scenario: Successful password reset

Given:
User has a valid reset token.

When:
User submits a valid new password.

Then:
Password should be updated.

Expected:
HTTP 200
```

## What makes it “sequential”?

The important part is this:

```text
PROMPT 1
   |
   | output
   ↓
USER STORY
   |
   | becomes input
   ↓
PROMPT 2
   |
   | output
   ↓
TASKS
   |
   | becomes input
   ↓
PROMPT 3
   |
   | output
   ↓
TECHNICAL DESIGN
   |
   | becomes input
   ↓
PROMPT 4
   |
   | output
   ↓
CODE
   |
   | becomes input
   ↓
PROMPT 5
   |
   | output
   ↓
TEST CASES
```

## In simple words
Sequential prompting means one prompt leads to another. Each prompt is more specific, and the output of one step becomes the input of the next. This keeps the task organized, easier to validate, and easier to debug.
