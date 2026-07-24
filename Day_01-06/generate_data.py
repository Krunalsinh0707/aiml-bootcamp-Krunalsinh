import csv
import random
from datetime import datetime, timedelta

random.seed(42)

first_names = [
    "Aarav",
    "Vivaan",
    "Rohan",
    "Priya",
    "Ananya",
    "Diya",
    "Krishna",
    "Meera",
]
last_names = ["Patel", "Shah", "Mori", "Singh", "Joshi", "Gupta", "Kumar", "Mehta"]

domain = ["@mail.codetrade.io", "@gmail.com", "@yahoo.com", "@sal.edu.in"]
start_date = datetime(2026, 1, 1)

with open("records.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        ["roll", "name", "email", "enrolled", "exam1", "exam2", "exam3", "exam4"]
    )

    for i in range(1, 201):
        roll = i
        name = f"{random.choice(first_names)}{random.choice(last_names)}"
        email = f"{name}{random.choice(domain)}"
        days = random.randint(0, 180)
        enrolled = start_date + timedelta(days=days)
        enrolled = enrolled.strftime("%d-%m-%Y")
        exam1 = random.randint(15, 100)
        exam2 = random.randint(15, 100)
        exam3 = random.randint(15, 100)
        exam4 = random.randint(15, 100)
        print(enrolled)
        print(roll, name)
        print(email)
        w.writerow([roll, name, email, enrolled, exam1, exam2, exam3, exam4])
