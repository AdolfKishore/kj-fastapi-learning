# FastAPI Learning Project

## 1. Project Overview

This project is a beginner-level backend application developed using FastAPI, a Python framework for building REST APIs.

The purpose of this project is to understand how APIs receive HTTP requests, process data, validate inputs, and return JSON responses.

The project is being developed as a practical exercise to learn FastAPI fundamentals.

## 2. Objectives

- Understand the fundamentals of FastAPI.
- Create and activate a Python virtual environment.
- Install and manage project dependencies.
- Implement HTTP GET and POST endpoints.
- Understand path parameters and query parameters.
- Validate request bodies using Pydantic models.
- Test API endpoints using Swagger UI.
- Learn how to implement CRUD operations.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language used for backend development |
| FastAPI | Framework for creating REST API endpoints |
| Uvicorn | ASGI server used to run the application |
| Pydantic | Validates incoming request data |
| VS Code | Code editor used for development |
| Swagger UI | Interactive interface for testing API endpoints |

## 4. Project Structure

```text
fastapi-learning/
├── venv/
├── main.py
├── requirements.txt
└── README.md
```

- `venv/`: Contains the project's Python virtual environment.
- `main.py`: Contains the FastAPI application and endpoint definitions.
- `requirements.txt`: Lists the installed Python package dependencies.
- `README.md`: Documents the project, setup instructions, and API functionality.

The virtual environment should not be committed to the Git repository.

## 5. Installation and Setup

### Prerequisites

- Python 3.13.14
- Visual Studio Code
- Python virtual environment support

### Step 1: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 2: Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```powershell
python -m pip install fastapi "uvicorn[standard]"
```

### Step 4: Generate the Dependency File

```powershell
python -m pip freeze > requirements.txt
```

### Step 5: Run the Application

```powershell
uvicorn main:app --reload
```

The application runs locally at:

`http://127.0.0.1:8000`

Interactive API documentation is available at:

`http://127.0.0.1:8000/docs`

## 6. Implemented Features

### 6.1 Home Endpoint

**Method:** GET

**Endpoint:** `/`

Returns a welcome message to verify that the API is running.

### 6.2 Retrieve All Students

**Method:** GET

**Endpoint:** `/students`

Returns the list of students stored in the application.

### 6.3 Retrieve a Student by ID

**Method:** GET

**Endpoint:** `/students/{student_id}`

Uses a path parameter to identify and retrieve a particular student.

### 6.4 Search Students by Department

**Method:** GET

**Endpoint:** `/search?department=CSE`

Uses a query parameter to filter students according to their department.

### 6.5 Create a Student

**Method:** POST

**Endpoint:** `/students`

Accepts student details as a JSON request body, validates the input using a Pydantic model, and adds the student to the in-memory collection.

Example request:

```json
{
  "name": "KJ",
  "department": "CSE"
}
```

The response contains a success message and the newly created student record.

### 6.6 Update a Student Using PUT

**Method:** PUT

**Endpoint:** `/students/{student_id}`

**Purpose:** Replaces an existing student's name and department using the supplied request body.

**Example request:**

```json
{
  "name": "Priya",
  "department": "CSE"
}
```

The endpoint returns the updated student record. If the requested student does not exist, it returns HTTP `404 Not Found`.

## 7. HTTP Concepts Practised

| Method | Purpose | Implementation status |
|---|---|---|
| GET | Retrieve data | Implemented |
| POST | Create data | Implemented |
| PUT | Replace existing data | Planned |
| PATCH | Partially update data | Planned |
| DELETE | Remove data | Planned |

## 8. Testing

The endpoints are tested through FastAPI's automatically generated Swagger UI.

Steps:

1. Start the application using Uvicorn.
2. Open `http://127.0.0.1:8000/docs`.
3. Select an endpoint.
4. Click **Try it out**.
5. Provide the required parameters or request body.
6. Click **Execute**.
7. Inspect the HTTP status code and response body.

## 9. Current Limitations

- Student records are stored in an in-memory Python list.
- Data is lost when the server restarts.
- A persistent database has not yet been integrated.
- Authentication and authorization have not been implemented.
- PUT, PATCH, and DELETE are pending implementation.
- Automated tests have not yet been added.

## 10. Future Improvements

- Implement PUT, PATCH, and DELETE operations.
- Improve error handling and HTTP status codes.
- Add automated API tests.
- Integrate a relational database.
- Introduce authentication and authorization.
- Explore integration with a Next.js frontend.

## 11. References

- FastAPI Documentation: <https://fastapi.tiangolo.com/>
- FastAPI First Steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- FastAPI Request Body: https://fastapi.tiangolo.com/tutorial/body/
- Uvicorn Documentation: https://www.uvicorn.org/
### Update a Student Using PATCH

**Endpoint:** `PATCH /students/{student_id}`

Updates only the fields supplied in the JSON request body, leaving other fields unchanged.

Example request:

```json
{
  "department": "ECE"
}
```

Returns the updated student record or a 404 error if the student does not exist.

### Delete a Student

**Endpoint:** `DELETE /students/{student_id}`

Removes the specified student from the in-memory collection and returns a confirmation message with the deleted record.

If the student does not exist, the endpoint returns HTTP 404 Not Found.
