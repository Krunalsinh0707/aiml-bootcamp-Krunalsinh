# from numpy import argsort
# import csv
# import numpy as np

# marks = []
# names = []
# domains = []

# with open("records.csv", newline="") as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# marks = np.array([[int(r[f"exam{i}"]) for i in range(1, 5)] for r in rows])

# names = [r["name"] for r in rows]

# domains = np.array([r["email"].split("@")[-1] for r in rows])

# unique_domains = np.unique(domains)


# exam_names = ["exam1", "exam2", "exam3", "exam4"]

# per_student = marks.mean(axis=1)

# per_exam = marks.mean(axis=0)

# exam_mean = np.mean(marks, axis=0)

# exam_std = np.std(marks, axis=0)

# standardized_marks = (marks - exam_mean) / exam_std

# curved_marks = np.clip(marks + 5, 0, 100)

# num_capped = np.sum(curved_marks == 100)

# hardest = np.argmin(per_exam)

# hardest_exam = exam_names[hardest]

# easiest_mark = np.argmax(per_exam)

# easiest_exam = exam_names[easiest_mark]

# passed = per_student >= 60

# top10 = per_student.argsort()[::-1][:10]

# top10_names = [names[i] for i in top10]


# for domain in unique_domains:
#     mask = domains == domain
#     avg = np.mean(per_student[mask])
#     print(domain, avg)

# print(marks.shape)

# print(per_student)

# print(per_exam)

# print(passed)
# print(top10_names)

# print("hardest exam", hardest_exam)

# print("Easiest-0z exam", easiest_exam)

# print(standardized_marks)

# print("Marks after applying curve:" , num_capped)

# print("Unique domains:", unique_domains)

# After the fuctioning

import csv
import numpy as np


def load_data(path: str) -> tuple[np.ndarray, list[str], np.ndarray]:
    """Load marks, student names, and email domains from a CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        A tuple containing:
            - marks array
            - list of student names
            - array of email domains
    """
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))

    marks = np.array([[int(r[f"exam{i}"]) for i in range(1, 5)] for r in rows])
    names = [r["name"] for r in rows]
    domains = np.array([r["email"].split("@")[-1] for r in rows])

    return marks, names, domains


def student_average(marks: np.ndarray) -> np.ndarray:
    """Calculate each student's average marks.

    Args:
        marks: Marks array.

    Returns:
        Array of student averages.
    """
    return marks.mean(axis=1)


def exam_average(marks: np.ndarray) -> np.ndarray:
    """Calculate the average marks for each exam.

    Args:
        marks: Marks array.

    Returns:
        Array of exam averages.
    """
    return marks.mean(axis=0)


def standardize_marks(marks: np.ndarray) -> np.ndarray:
    """Standardize marks for each exam.

    Args:
        marks: Marks array.

    Returns:
        Standardized marks array.
    """
    mean = np.mean(marks, axis=0)
    std = np.std(marks, axis=0)
    return (marks - mean) / std


def curve_marks(marks: np.ndarray) -> tuple[np.ndarray, int]:
    """Apply a 5-mark curve capped at 100.

    Args:
        marks: Marks array.

    Returns:
        Curved marks and number of capped scores.
    """
    curved = np.clip(marks + 5, 0, 100)
    capped = np.sum(curved == 100)
    return curved, capped


def hardest_exam(per_exam: np.ndarray, exam_names: list[str]) -> str:
    """Return the hardest exam.

    Args:
        per_exam: Average score of each exam.
        exam_names: Exam names.

    Returns:
        Hardest exam name.
    """
    return exam_names[np.argmin(per_exam)]


def easiest_exam(per_exam: np.ndarray, exam_names: list[str]) -> str:
    """Return the easiest exam.

    Args:
        per_exam: Average score of each exam.
        exam_names: Exam names.

    Returns:
        Easiest exam name.
    """
    return exam_names[np.argmax(per_exam)]


def passing_students(per_student: np.ndarray) -> np.ndarray:
    """Determine which students passed.

    Args:
        per_student: Student averages.

    Returns:
        Boolean array indicating pass/fail.
    """
    return per_student >= 60


def top_students(
    per_student: np.ndarray,
    names: list[str],
    n: int = 10,
) -> list[str]:
    """Return the names of the top students.

    Args:
        per_student: Student averages.
        names: Student names.
        n: Number of students to return.

    Returns:
        List of top student names.
    """
    indices = per_student.argsort()[::-1][:n]
    return [names[i] for i in indices]


def compare_domains(domains: np.ndarray, per_student: np.ndarray) -> None:
    """Print average marks for each email domain.

    Args:
        domains: Email domains.
        per_student: Student averages.
    """
    for domain in np.unique(domains):
        mask = domains == domain
        print(domain, np.mean(per_student[mask]))


def main() -> None:
    """Run the complete analysis."""

    exam_names = ["exam1", "exam2", "exam3", "exam4"]

    marks, names, domains = load_data("records.csv")

    per_student = student_average(marks)
    per_exam = exam_average(marks)

    standardized = standardize_marks(marks)

    curved, capped = curve_marks(marks)

    print("Shape:", marks.shape)
    print("Student averages:", per_student)
    print("Exam averages:", per_exam)
    print("Passed:", passing_students(per_student))
    print("Top 10:", top_students(per_student, names))
    print("Hardest exam:", hardest_exam(per_exam, exam_names))
    print("Easiest exam:", easiest_exam(per_exam, exam_names))

    compare_domains(domains, per_student)

    print("Standardized marks:")
    print(standardized)

    print("Marks capped at 100:", capped)
    print("Unique domains:", np.unique(domains))


if __name__ == "__main__":
    main()
