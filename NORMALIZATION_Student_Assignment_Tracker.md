# Normalization Report

## Project Name

Student Assignment Tracker System

## Purpose

The purpose of normalization is to organize the database into well-structured related tables, reduce duplicate data, prevent anomalies, and maintain data integrity. The final application uses three main relational tables: students, courses, and assignments.

---

## Starting Schema Summary

The original Project 2 SQL design included the following major data areas:

- Student information
- Course information
- Assignment information
- Assignment submission and grading details

If all of this data were stored in one large table, student and course details would be repeated across multiple assignment rows. Therefore, the schema was separated into normalized tables.

---

## Original Functional Dependencies

### Students

- student_id -> student_name, email, created_at
- email -> student_id, student_name, created_at

### Courses

- course_id -> course_name, instructor, created_at

### Assignments

- assignment_id -> student_id, course_id, title, due_date, submission_date, marks, delay_days, status, created_at

### Relationship Dependencies

- student_id identifies the student connected to an assignment
- course_id identifies the course connected to an assignment
- assignment_id identifies the assignment submission and grading information

---

## Anomaly Identification

### Update Anomaly

If student or course information were repeated in an assignment table, changing one student's email or one instructor's name would require updating multiple rows. Missing one row could create inconsistent information.

### Insertion Anomaly

If students and courses were stored only inside an assignment table, a new student or course could not be added unless an assignment also existed.

### Deletion Anomaly

If the only assignment for a student or course were deleted, student or course information could also be lost if everything were stored in one table.

---

## First Normal Form (1NF)

The schema satisfies 1NF because:

- Each table has a primary key.
- Each field stores atomic values.
- There are no repeating groups.
- Each row represents a single record.

Examples:

- One row in students represents one student.
- One row in courses represents one course.
- One row in assignments represents one assignment.

---

## Second Normal Form (2NF)

The schema satisfies 2NF because:

- It is already in 1NF.
- Each non-key attribute fully depends on the whole primary key.
- There are no partial dependencies.

Examples:

- student_name and email depend only on student_id.
- course_name and instructor depend only on course_id.
- title, due_date, marks, and status depend only on assignment_id.

---

## Third Normal Form (3NF)

The schema satisfies 3NF because:

- It is already in 2NF.
- There are no transitive dependencies.
- Non-key attributes do not depend on other non-key attributes.

Examples:

- Student details are stored only in the students table.
- Course details are stored only in the courses table.
- Assignments reference students and courses using foreign keys instead of repeating their details.

---

## Decomposition Steps

### Step 1: Separate Student Data

Student-related attributes were placed in the students table:

- student_id
- student_name
- email
- created_at

### Step 2: Separate Course Data

Course-related attributes were placed in the courses table:

- course_id
- course_name
- instructor
- created_at

### Step 3: Separate Assignment Data

Assignment-related attributes were placed in the assignments table:

- assignment_id
- student_id
- course_id
- title
- due_date
- submission_date
- marks
- delay_days
- status
- created_at

### Step 4: Add Foreign Keys

The assignments table uses:

- student_id as a foreign key referencing students(student_id)
- course_id as a foreign key referencing courses(course_id)

This supports relationship management while avoiding repeated student and course data.

---

## Final Relational Schema

### students

| Column | Description |
|---|---|
| student_id | Primary key |
| student_name | Student full name |
| email | Unique student email |
| created_at | Date student record was created |

### courses

| Column | Description |
|---|---|
| course_id | Primary key |
| course_name | Course name |
| instructor | Instructor name |
| created_at | Date course record was created |

### assignments

| Column | Description |
|---|---|
| assignment_id | Primary key |
| student_id | Foreign key referencing students |
| course_id | Foreign key referencing courses |
| title | Assignment title |
| due_date | Assignment due date |
| submission_date | Assignment submission date |
| marks | Assignment marks |
| delay_days | Number of late days |
| status | Assignment status |
| created_at | Date assignment record was created |

---

## Relationship Management

### Students to Assignments

One student can have many assignments.

Relationship:

students.student_id -> assignments.student_id

### Courses to Assignments

One course can have many assignments.

Relationship:

courses.course_id -> assignments.course_id

---

## Data Integrity Rules

The final schema supports data integrity through:

- Primary keys
- Foreign keys
- Unique student emails
- NOT NULL constraints for required fields
- CHECK constraints for marks and delay_days
- Controlled assignment status values

---

## Conclusion

The Student Assignment Tracker database is normalized up to Third Normal Form. The final design reduces redundancy, prevents insertion, update, and deletion anomalies, and supports a clean relational structure for the Flask application.
