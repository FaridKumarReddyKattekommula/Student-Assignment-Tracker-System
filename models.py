# SQLAlchemy models file
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.String(20), nullable=False)

    assignments = db.relationship(
        "Assignment",
        backref="student",
        cascade="all, delete-orphan"
    )


class Course(db.Model):
    __tablename__ = "courses"

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(20), nullable=False)

    assignments = db.relationship(
        "Assignment",
        backref="course",
        cascade="all, delete-orphan"
    )


class Assignment(db.Model):
    __tablename__ = "assignments"

    assignment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.course_id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)
    submission_date = db.Column(db.String(20), nullable=True)
    marks = db.Column(db.Float, nullable=True)
    delay_days = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default="Pending")
    created_at = db.Column(db.String(20), nullable=False)