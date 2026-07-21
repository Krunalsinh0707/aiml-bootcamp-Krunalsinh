from student import Student


def test_add_mark():
    student = Student("Krunal", 101)
    student.add_mark(90)

    assert student.marks == [90]


def test_average():
    student = Student("Krunal", 101)

    student.add_mark(80)
    student.add_mark(100)

    assert student.average() == 90.0


def test_average_empty():
    student = Student("Krunal", 101)

    assert student.average() == 0


def test_str():
    student = Student("Krunal", 101)
    student.add_mark(90)

    assert "Krunal" in str(student)
