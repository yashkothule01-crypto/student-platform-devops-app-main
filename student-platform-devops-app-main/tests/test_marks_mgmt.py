from services.student_service import get_all_marks, get_marks_by_student


def test_get_all_marks_returns_sample_marks():
    marks = get_all_marks()

    assert len(marks) >= 3
    assert marks[0]["student_id"] == 1
    assert marks[0]["grade"] == "A"


def test_get_marks_for_valid_student():
    marks = get_marks_by_student(2)

    assert marks is not None
    assert marks["student_name"] == "Rahul Mehta"
    assert marks["subjects"]["Neural Networks"] == 81


def test_get_marks_for_non_existing_student_returns_none():
    marks = get_marks_by_student(999)

    assert marks is None
