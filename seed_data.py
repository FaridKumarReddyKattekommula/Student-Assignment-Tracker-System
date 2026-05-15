from app import app
from models import db, Student, Course, Assignment
from datetime import date

with app.app_context():

    db.create_all()

    student1 = Student(
        student_name="Varun",
        email="varun@gmail.com",
        created_at=str(date.today())
    )

    student2 = Student(
        student_name="Mahesh",
        email="example@gmail.com",
        created_at=str(date.today())
    )

    course1 = Course(
        course_name="Database Systems",
        instructor="Dr. Williams",
        created_at=str(date.today())
    )

    course2 = Course(
        course_name="Web Development",
        instructor="Prof. Anderson",
        created_at=str(date.today())
    )

    db.session.add(student1)
    db.session.add(student2)

    db.session.add(course1)
    db.session.add(course2)

    db.session.commit()

    assignment1 = Assignment(
        student_id=1,
        course_id=1,
        title="ER Diagram Project",
        due_date="2026-05-20",
        submission_date="2026-05-19",
        marks=92,
        delay_days=0,
        status="Submitted",
        created_at=str(date.today())
    )

    assignment2 = Assignment(
        student_id=2,
        course_id=2,
        title="Flask CRUD Application",
        due_date="2026-05-22",
        submission_date="2026-05-19",
        marks=95,
        delay_days=0,
        status="Submitted",
        created_at=str(date.today())
    )

    db.session.add(assignment1)
    db.session.add(assignment2)

    db.session.commit()

    print("Sample data inserted successfully")