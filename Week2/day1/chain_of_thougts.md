# Chain-of-Thought Prompting

## Simple example: calculate the final price

### Problem
A product costs ₹1,000. It has a 20% discount, and then 18% GST is added. What is the final price?

### Prompt
```text
You are a math problem-solving assistant.

Solve the following problem step by step.

Problem:
A product costs ₹1,000.
It has a 20% discount.
After the discount, 18% GST is added.

Find the final price.

Check your calculations before giving the final answer.
```

### Reasoning flow
```text
Original price
    ↓
Calculate 20% discount
    ↓
Subtract discount
    ↓
Calculate 18% GST
    ↓
Add GST
    ↓
Final price
```

### Result
- Original price = ₹1,000
- 20% discount = ₹200
- Price after discount = ₹800
- 18% GST on ₹800 = ₹144
- Final price = ₹944

## Simple definition
Chain-of-Thought Prompting means asking an AI to solve a problem by showing its reasoning in a step-by-step flow instead of jumping directly to the answer.

For IT and software development, a simple CoT workflow could look like:

Requirement → Analyze → Identify components → Design solution → Check edge cases → Final solution

## CoT vs. Sequential Prompting

| Type | How it works | Best use |
|---|---|---|
| Chain-of-Thought | Reasoning happens inside one prompt | Complex problem-solving in one flow |
| Sequential Prompting | The task is split into multiple prompts | Multi-step workflows with handoff between steps |

In short, CoT keeps reasoning in one prompt, while sequential prompting uses several prompts where each output becomes the next input.