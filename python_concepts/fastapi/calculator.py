# Genearte fastAPI for Simple calculator
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Calculator API"}


# Method must be POST to perform calculations
@app.post("/calculate")
async def calculate(data: dict):
    a = data.get("num1")
    b = data.get("num2")
    operation = data.get("operation")

    if operation == "add":
        return {"result": a + b}
    elif operation == "subtract":
        return {"result": a - b}
    elif operation == "multiply":
        return {"result": a * b}
    elif operation == "divide":
        if b != 0:
            return {"result": a / b}
        else:
            return {"error": "Division by zero is not allowed"}
    else:
        return {"error": "Invalid operation"}


    # E:\Projects\Naveen_Repo\python_learning\python_concepts\fastapi\calculator.py