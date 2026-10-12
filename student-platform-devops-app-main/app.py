from datetime import datetime

from flask import Flask, jsonify, render_template, request

from services.student_service import (
    get_all_courses,
    get_all_marks,
    get_all_students,
    get_marks_by_student,
    get_student_by_id,
)


app = Flask(__name__)


def wants_json_response():
    if request.args.get("format") == "json":
        return True

    best_match = request.accept_mimetypes.best_match(["text/html", "application/json"])
    return (
        best_match == "application/json"
        and request.accept_mimetypes[best_match] > request.accept_mimetypes["text/html"]
    )


def not_found_response(message):
    if wants_json_response():
        return jsonify({"error": message}), 404

    return render_template("404.html", message=message, active_page=""), 404


@app.context_processor
def inject_layout_data():
    return {
        "current_year": datetime.now().year,
        "nav_items": [
            {
                "label": "Dashboard",
                "endpoint": "home",
                "icon": "bi-speedometer2",
                "active_page": "dashboard",
            },
            {
                "label": "Students",
                "endpoint": "students",
                "icon": "bi-people",
                "active_page": "students",
            },
            {
                "label": "Courses",
                "endpoint": "courses",
                "icon": "bi-journal-bookmark",
                "active_page": "courses",
            },
            {
                "label": "Marks",
                "endpoint": "marks",
                "icon": "bi-clipboard-data",
                "active_page": "marks",
            },
        ],
    }


@app.route("/")
def home():
    students_data = get_all_students()
    courses_data = get_all_courses()
    marks_data = get_all_marks()

    if wants_json_response():
        return jsonify(
            {
                "application": "Student Record & Academic Management Platform",
                "status": "Running",
            }
        )

    stats = [
        {
            "label": "Total Students",
            "value": len(students_data),
            "description": "Active academic records",
            "icon": "bi-people-fill",
            "tone": "primary",
        },
        {
            "label": "Total Courses",
            "value": len(courses_data),
            "description": "AIML-focused programs",
            "icon": "bi-journal-richtext",
            "tone": "info",
        },
        {
            "label": "Marks Records",
            "value": len(marks_data),
            "description": "Performance entries",
            "icon": "bi-clipboard-check",
            "tone": "success",
        },
        {
            "label": "System Status",
            "value": "Healthy",
            "description": "All services operational",
            "icon": "bi-activity",
            "tone": "success",
        },
    ]

    return render_template(
        "index.html",
        active_page="dashboard",
        students=students_data,
        stats=stats,
    )


@app.route("/students")
def students():
    students_data = get_all_students()

    if wants_json_response():
        return jsonify(students_data)

    return render_template(
        "students.html",
        active_page="students",
        students=students_data,
    )


@app.route("/students/<int:student_id>")
def student_detail(student_id):
    student = get_student_by_id(student_id)
    if student is None:
        return not_found_response(f"Student with id {student_id} was not found")

    if wants_json_response():
        return jsonify(student)

    marks_record = get_marks_by_student(student_id)
    return render_template(
        "student_detail.html",
        active_page="students",
        student=student,
        marks_record=marks_record,
    )


@app.route("/courses")
def courses():
    courses_data = get_all_courses()

    if wants_json_response():
        return jsonify(courses_data)

    return render_template(
        "courses.html",
        active_page="courses",
        courses=courses_data,
    )


@app.route("/marks")
def marks():
    marks_data = get_all_marks()

    if wants_json_response():
        return jsonify(marks_data)

    return render_template(
        "marks.html",
        active_page="marks",
        marks=marks_data,
    )


@app.route("/marks/<int:student_id>")
def student_marks(student_id):
    marks_record = get_marks_by_student(student_id)
    if marks_record is None:
        return not_found_response(f"Marks for student id {student_id} were not found")

    if wants_json_response():
        return jsonify(marks_record)

    student = get_student_by_id(student_id)
    return render_template(
        "marks_student.html",
        active_page="marks",
        student=student,
        marks_record=marks_record,
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "404.html",
        message="The requested academic record could not be found.",
        active_page="",
    ), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
