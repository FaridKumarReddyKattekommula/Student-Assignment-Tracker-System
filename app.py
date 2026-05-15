# Flask application file
import os
from datetime import date
from flask import Flask, render_template, request, redirect
from models import db, Student, Course, Assignment

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, "student_tracker.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database tables created successfully")


@app.route("/")
def dashboard():
    total_students = Student.query.count()
    total_courses = Course.query.count()
    total_assignments = Assignment.query.count()
    pending_assignments = Assignment.query.filter_by(status="Pending").count()
    completed_assignments = Assignment.query.filter(
        Assignment.status.in_(["Submitted", "Late", "Graded"])
    ).count()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        total_courses=total_courses,
        total_assignments=total_assignments,
        pending_assignments=pending_assignments,
        completed_assignments=completed_assignments
    )


@app.route("/students", methods=["GET", "POST"])
def students():
    message = ""

    if request.method == "POST":
        student_name = request.form["student_name"].strip()
        email = request.form["email"].strip()

        existing_student = Student.query.filter_by(email=email).first()

        if student_name == "":
            message = "Student name is required."
        elif existing_student:
            message = "Email already exists. Please use a different email."
        else:
            new_student = Student(
                student_name=student_name,
                email=email,
                created_at=str(date.today())
            )

            db.session.add(new_student)
            db.session.commit()

            return redirect("/students")

    students_list = Student.query.all()

    return render_template(
        "students.html",
        students=students_list,
        message=message
    )


@app.route("/edit_student/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    message = ""

    if request.method == "POST":
        student_name = request.form["student_name"].strip()
        email = request.form["email"].strip()

        existing_student = Student.query.filter(
            Student.email == email,
            Student.student_id != student_id
        ).first()

        if student_name == "":
            message = "Student name is required."
        elif existing_student:
            message = "Email already exists. Please use a different email."
        else:
            student.student_name = student_name
            student.email = email

            db.session.commit()

            return redirect("/students")

    return render_template(
        "edit_student.html",
        student=student,
        message=message
    )


@app.route("/delete_student/<int:student_id>")
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)

    db.session.delete(student)
    db.session.commit()

    return redirect("/students")


@app.route("/courses", methods=["GET", "POST"])
def courses():
    message = ""

    if request.method == "POST":
        course_name = request.form["course_name"].strip()
        instructor = request.form["instructor"].strip()

        if course_name == "" or instructor == "":
            message = "Course name and instructor are required."
        else:
            new_course = Course(
                course_name=course_name,
                instructor=instructor,
                created_at=str(date.today())
            )

            db.session.add(new_course)
            db.session.commit()

            return redirect("/courses")

    courses_list = Course.query.all()

    return render_template(
        "courses.html",
        courses=courses_list,
        message=message
    )


@app.route("/edit_course/<int:course_id>", methods=["GET", "POST"])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    message = ""

    if request.method == "POST":
        course_name = request.form["course_name"].strip()
        instructor = request.form["instructor"].strip()

        if course_name == "" or instructor == "":
            message = "Course name and instructor are required."
        else:
            course.course_name = course_name
            course.instructor = instructor

            db.session.commit()

            return redirect("/courses")

    return render_template(
        "edit_course.html",
        course=course,
        message=message
    )


@app.route("/delete_course/<int:course_id>")
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)

    db.session.delete(course)
    db.session.commit()

    return redirect("/courses")


@app.route("/assignments", methods=["GET", "POST"])
def assignments():
    message = ""

    if request.method == "POST":
        student_id = int(request.form["student_id"])
        course_id = int(request.form["course_id"])
        title = request.form["title"].strip()
        due_date = request.form["due_date"]
        submission_date = request.form["submission_date"]
        marks_input = request.form["marks"]
        status = request.form["status"]

        marks = None
        if marks_input != "":
            marks = float(marks_input)

        delay_days = 0
        if submission_date and due_date and submission_date > due_date:
            delay_days = (
                date.fromisoformat(submission_date)
                - date.fromisoformat(due_date)
            ).days

        if title == "":
            message = "Assignment title is required."
        elif marks is not None and marks < 0:
            message = "Marks cannot be negative."
        else:
            new_assignment = Assignment(
                student_id=student_id,
                course_id=course_id,
                title=title,
                due_date=due_date,
                submission_date=submission_date,
                marks=marks,
                delay_days=delay_days,
                status=status,
                created_at=str(date.today())
            )

            db.session.add(new_assignment)
            db.session.commit()

            return redirect("/assignments")

    assignments_list = Assignment.query.all()
    students_list = Student.query.all()
    courses_list = Course.query.all()

    return render_template(
        "assignments.html",
        assignments=assignments_list,
        students=students_list,
        courses=courses_list,
        message=message
    )


@app.route("/delete_assignment/<int:assignment_id>")
def delete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)

    db.session.delete(assignment)
    db.session.commit()

    return redirect("/assignments")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)