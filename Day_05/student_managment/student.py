"""
Student management module.

This module provides a Student class for storing student details,
adding marks, and calculating average marks.
"""


class Student:

    def __init__(self, name: str, roll: int, marks: list[int] | None = None):
        """
        Initialize a Student object.

        Args:
            name: Student's name.
            roll: Student's roll number.
            marks: Optional list of marks.

        Returns:
            None.
        """
        self.name = name
        self.roll = roll
        self.marks = marks if marks is not None else []

    def add_mark(self, score: int) -> None:
        """
        Add a mark to the student's record.

        Args:
            score: Student's mark.

        Returns:
            None.
        """
        if score < 0 or score > 100:
            raise ValueError("Marks must be between 0 and 100.")
        self.marks.append(score)

    def average(self) -> float:
        """
        Calculate the student's average marks.

        Returns:
            The average of all marks. Returns 0.0 if no marks exist.
        """
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def __str__(self) -> str:
        """
        Return a readable string representation of the student.

        Returns:
            A formatted string containing student details.
        """
        return (
            f"Student Name: {self.name}, "
            f"Roll Number: {self.roll}, "
            f"Marks: {self.marks}, "
            f"Average: {self.average():.2f}"
        )

    # def __repr__(self):
    # return f"Student('{self.name}', {self.roll}, {self.marks})"
