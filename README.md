# Expense Tracker API

A RESTful API built with FastAPI that allows users to manage their personal expenses. Users can create, view, update, and delete expense records. The project was built to learn backend development, REST API design, and database integration using Python.

## Features

- Create a new expense
- View all expenses
- View a single expense
- Update an expense
- Delete an expense
- Store data in PostgreSQL
- Request validation with Pydantic

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd expense-tracker-api
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install PostgreSQL

Download and install PostgreSQL from:

https://www.postgresql.org/download/

Create a database and update your database connection string in your configuration file.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```


