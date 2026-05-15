# Student Assignment Tracker System

## Project Description

The Student Assignment Tracker System is a full-stack web application developed using Python, Flask, SQLite, SQLAlchemy, HTML5, CSS3, and Jinja2 templates.

The application is designed for students, instructors, and academic administrators to efficiently manage students, courses, and assignments in a relational database system.

The system supports:

- Student management
- Course management
- Assignment tracking
- Dashboard summaries
- CRUD operations
- Relational database handling
- Data validation
- Transaction management
- Aggregate reporting

---

# GitHub Repository

Repository URL:

https://github.com/FaridKumarReddyKattekommula/Student-Assignment-Tracker-System

Commit Activity:

https://github.com/FaridKumarReddyKattekommula/Student-Assignment-Tracker-System/graphs/commit-activity

---

# Technical Stack

- Python 3
- Flask
- SQLite
- SQLAlchemy
- HTML5
- CSS3
- Jinja2 Templates
- Git
- GitHub

---

# Main Modules

The application contains the following modules:

- Dashboard
- Students
- Courses
- Assignments

---

# Features

## Dashboard

The dashboard displays high-level database insights using aggregate functions.

Displayed metrics include:

- Total Students
- Total Courses
- Total Assignments
- Pending Assignments
- Completed Assignments

The dashboard uses SQL aggregate operations such as:

- COUNT()
- SUM()
- AVG()

---

# Student Management

Users can:

- Add students
- View student records
- Edit student information
- Delete student records

---

# Course Management

Users can:

- Add courses
- View course records
- Edit course information
- Delete course records

---

# Assignment Management

Users can:

- Add assignments
- View assignment records
- Delete assignment records
- Associate assignments with students and courses
- Track assignment due dates
- Track submission dates
- Calculate delay days
- Store assignment marks
- Store assignment status

---

# CRUD Operations

The project supports CRUD operations across multiple related tables.

## Students

- Create
- Read
- Update
- Delete

## Courses

- Create
- Read
- Update
- Delete

## Assignments

- Create
- Read
- Delete

---

# Relationship Management

The project implements One-to-Many relationships.

## Relationships

- One student can have multiple assignments.
- One course can have multiple assignments.

The assignments table uses foreign keys to maintain relational integrity between students and courses.

---

# Transaction Logic

When a new assignment is added:

1. Student validation occurs.
2. Course validation occurs.
3. Assignment title validation occurs.
4. Delay days are calculated.
5. Assignment marks are validated.
6. Assignment status is validated.
7. Database transaction commits only after successful validation.

This ensures transactional consistency and prevents invalid data insertion.

---

# Data Validation

The application performs server-side validation including:

- Required field validation
- Unique student email validation
- Empty string prevention
- Negative marks prevention
- Assignment title validation
- Course validation
- Student validation

---

# Database Design

The database is normalized to Third Normal Form (3NF).

Main tables:

- students
- courses
- assignments

The relational schema is included in:

---
# schema structure

schema.sql