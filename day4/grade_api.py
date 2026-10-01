# python -m uvicorn python_concepts.fastapi.grade_api:app --reload
import csv
import io

from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel, Field

app = FastAPI(title="Student Grade API")


class Student(BaseModel):
    name: str = Field(min_length=1)
    mark: float = Field(ge=0, le=100)


class GradeRequest(BaseModel):
    students: list[Student] = Field(min_length=1)


def grade_for_mark(mark: float) -> str:
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def build_results(students: list[Student]) -> list[dict]:
    return [
        {"Name": student.name, "Mark": student.mark,
         "Grade": grade_for_mark(student.mark)}
        for student in students
    ]


@app.post("/grades/calculate")
def calculate_grades(request: GradeRequest):
    results = build_results(request.students)
    average = sum(row["Mark"] for row in results) / len(results)
    return {
        "results": results,
        "average_mark": round(average, 2),
        "average_grade": grade_for_mark(average),
    }


@app.post("/grades/csv")
def download_grades_csv(request: GradeRequest):
    results = build_results(request.students)
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["Name", "Mark", "Grade"])
    writer.writeheader()
    writer.writerows(results)

    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=student_results.csv"},
    )


# Need to run the FastAPI server before using this Streamlit app. Use the following command to start the server:
# python -m uvicorn grade_api:app --reload
# Need to run the Streamlit app with the following command: 
# streamlit run day4/student_grade_manager.py