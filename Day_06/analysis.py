import numpy as np

# Set seed for reproducibility
np.random.seed(42)


marks = np.random.randint(
    30, 101, size=(100, 5)
)  # Generate marks for 100 students and 5 exams


student_avg = np.mean(marks, axis=1)  # Average marks of each student


exam_avg = np.mean(marks, axis=0)  # Average marks of each exam


passed = student_avg >= 60


num_passed = np.sum(passed)  # Count passed students


fraction_passed = num_passed / len(student_avg)  # Fraction of students passed

top10_indices = np.argsort(student_avg)[-10:][::-1]


top10_scores = student_avg[top10_indices]  # Corresponding average scores


exam_mean = np.mean(marks, axis=0)  # Mean for each exam (column)

exam_std = np.std(marks, axis=0)  # standard deviation for each exam (column)


standardized_marks = (marks - exam_mean) / exam_std  # Standardize marks


curved_marks = np.clip(marks + 5, 0, 100)  # Add 5 marks and cap at 100

num_capped = np.sum(curved_marks == 100)  # Count how many marks hit the cap (100)

failed_mask = marks < 40  # Mask: True where a student failed an exam (< 40)

failed_all = np.all(failed_mask, axis=1)  # Students who failed every exam

failed_students = np.where(failed_all)[0]  # Indices of those students

print("Shape:", marks.shape)

print("\nFirst 10 students' marks:")

print(marks[:10])

print("Student Averages:", student_avg)

print("\nExam Averages:", exam_avg)

print("Students Passed:", num_passed)

print("Fraction Passed:", fraction_passed)

print("Percentage Passed:", fraction_passed * 100, "%")

print("Top 10 Student Indices:", top10_indices)

print("\nTop 10 Average Scores:", top10_scores)

print("Standardized Marks:", standardized_marks)

# Verify
print("\nMean of each exam:")

print(np.mean(standardized_marks, axis=0))

print("\nStandard deviation of each exam:")

print(np.std(standardized_marks, axis=0))

print("Marks after applying curve:")

print(curved_marks)

print("\nNumber of marks capped at 100:", num_capped)

print("Students who failed every exam:", failed_students)
