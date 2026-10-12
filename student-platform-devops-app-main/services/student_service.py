from copy import deepcopy


STUDENTS = [
    {
        "id": 1,
        "name": "Ananya Rao",
        "email": "ananya.rao@example.edu",
        "course": "B.Tech AIML",
        "year": 2,
    },
    {
        "id": 2,
        "name": "Rahul Mehta",
        "email": "rahul.mehta@example.edu",
        "course": "B.Sc Artificial Intelligence",
        "year": 3,
    },
    {
        "id": 3,
        "name": "Sara Khan",
        "email": "sara.khan@example.edu",
        "course": "B.Tech Data Science and AIML",
        "year": 1,
    },
]


COURSES = [
    {
        "id": 101,
        "name": "B.Tech AIML",
        "duration": "4 years",
        "department": "Artificial Intelligence and Machine Learning",
    },
    {
        "id": 102,
        "name": "B.Sc Artificial Intelligence",
        "duration": "3 years",
        "department": "Computer Science",
    },
    {
        "id": 103,
        "name": "B.Tech Data Science and AIML",
        "duration": "4 years",
        "department": "Data Science",
    },
]


MARKS = [
    {
        "student_id": 1,
        "student_name": "Ananya Rao",
        "subjects": {
            "Machine Learning": 88,
            "Python Programming": 92,
            "Data Structures": 84,
        },
        "total": 264,
        "grade": "A",
    },
    {
        "student_id": 2,
        "student_name": "Rahul Mehta",
        "subjects": {
            "Neural Networks": 81,
            "Database Management": 78,
            "Statistics": 86,
        },
        "total": 245,
        "grade": "B+",
    },
    {
        "student_id": 3,
        "student_name": "Sara Khan",
        "subjects": {
            "Introduction to AIML": 91,
            "Python Programming": 89,
            "Mathematics for AI": 94,
        },
        "total": 274,
        "grade": "A+",
    },
]


def get_all_students():
    return deepcopy(STUDENTS)


def get_student_by_id(student_id):
    student = next((student for student in STUDENTS if student["id"] == student_id), None)
    return deepcopy(student) if student else None


def get_all_courses():
    return deepcopy(COURSES)


def get_all_marks():
    return deepcopy(MARKS)


def get_marks_by_student(student_id):
    if get_student_by_id(student_id) is None:
        return None

    marks = next((marks for marks in MARKS if marks["student_id"] == student_id), None)
    return deepcopy(marks) if marks else None
