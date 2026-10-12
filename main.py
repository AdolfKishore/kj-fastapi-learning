
from fastapi import FastAPI

app = FastAPI(title="FastAPI Learning Project")

# Sample data
students = [
    {"id": 1, "name": "Kumar", "department": "CSE"},
    {"id": 2, "name": "Priya", "department": "IT"},
    {"id": 3, "name": "Arun", "department": "CSE"},
]


# GET 1: Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI project"}


# GET 2: Retrieve all students
@app.get("/students")
def get_students():
    return students


# GET 3: Retrieve a student by ID (path parameter)
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"error": "Student not found"}


# GET 4: Filter students by department (query parameter)
@app.get("/search")
def search_students(department: str):
    result = [
        student for student in students
        if student["department"].lower() == department.lower()
    ]
    return result


from pydantic import BaseModel


# Defines the structure of incoming student data
class Student(BaseModel):
    name: str
    department: str


# POST: Create a new student
@app.post("/students")
def create_student(student: Student):
    new_id = max(
        (item["id"] for item in students),
        default=0
    ) + 1

    new_student = {
        "id": new_id,
        **student.model_dump()
    }

    students.append(new_student)

    return {
        "message": "Student created successfully",
        "student": new_student
    }

from fastapi import HTTPException, status


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for index, existing_student in enumerate(students):
        if existing_student["id"] == student_id:
            updated_student = {
                "id": student_id,
                **student.model_dump()
            }

            students[index] = updated_student
            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )

# Request model for partial updates
class StudentPatch(BaseModel):
    name: str | None = None
    department: str | None = None


# PATCH: Update selected student fields
@app.patch("/students/{student_id}")
def patch_student(student_id: int, student: StudentPatch):
    for existing_student in students:
        if existing_student["id"] == student_id:
            updates = student.model_dump(exclude_unset=True)

            if not updates:
                raise HTTPException(
                    status_code=400,
                    detail="No fields provided for update"
                )

            existing_student.update(updates)

            return {
                "message": "Student partially updated",
                "student": existing_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
