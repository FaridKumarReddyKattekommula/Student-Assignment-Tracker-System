-- =========================================================
-- STUDENT ASSIGNMENT TRACKER SYSTEM
-- FINAL 3NF SCHEMA.SQL
-- =========================================================

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;

-- =========================================================
-- STUDENTS TABLE
-- Stores one record per student.
-- =========================================================
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at DATE NOT NULL
);

-- =========================================================
-- COURSES TABLE
-- Stores one record per course.
-- =========================================================
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor TEXT NOT NULL,
    created_at DATE NOT NULL
);

-- =========================================================
-- ASSIGNMENTS TABLE
-- Stores assignment records and links each assignment
-- to one student and one course.
-- =========================================================
CREATE TABLE assignments (
    assignment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    due_date DATE NOT NULL,
    submission_date DATE,
    marks REAL,
    delay_days INTEGER DEFAULT 0,
    status TEXT DEFAULT 'Pending',
    created_at DATE NOT NULL,

    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (course_id) REFERENCES courses(course_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CHECK (marks IS NULL OR marks >= 0),
    CHECK (delay_days >= 0),
    CHECK (status IN ('Pending', 'Submitted', 'Late', 'Graded'))
);

-- =========================================================
-- SAMPLE DATA
-- =========================================================

INSERT INTO students
(student_id, student_name, email, created_at)
VALUES
(1, 'Alice Johnson', 'alice@example.com', '2026-01-05'),
(2, 'Brian Lee', 'brian@example.com', '2026-01-06'),
(3, 'Carla Davis', 'carla@example.com', '2026-01-07'),
(4, 'David Smith', 'david@example.com', '2026-01-08'),
(5, 'Emma Wilson', 'emma@example.com', '2026-01-09');

INSERT INTO courses
(course_id, course_name, instructor, created_at)
VALUES
(101, 'Database Systems', 'Dr. Brown', '2026-01-10'),
(102, 'Python Programming', 'Dr. Green', '2026-01-11'),
(103, 'Web Development', 'Dr. White', '2026-01-12'),
(104, 'Statistics', 'Dr. Black', '2026-01-13'),
(105, 'Data Visualization', 'Dr. Adams', '2026-01-14');

INSERT INTO assignments
(
    assignment_id,
    student_id,
    course_id,
    title,
    due_date,
    submission_date,
    marks,
    delay_days,
    status,
    created_at
)
VALUES
(1001, 1, 101, 'SQL Basics', '2026-02-10', '2026-02-09', 88.00, 0, 'Graded', '2026-02-01'),
(1002, 2, 101, 'ER Diagram', '2026-02-12', '2026-02-12', 92.00, 0, 'Graded', '2026-02-02'),
(1003, 3, 102, 'Python Loops', '2026-02-15', '2026-02-14', 85.00, 0, 'Graded', '2026-02-03'),
(1004, 4, 103, 'HTML Form', '2026-02-18', '2026-02-20', 78.00, 2, 'Late', '2026-02-04'),
(1005, 5, 104, 'Data Summary', '2026-02-22', '2026-02-23', 95.00, 1, 'Late', '2026-02-05');
