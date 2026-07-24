# import csv, re
# from collections import Counter, defaultdict
# from datetime import datetime

# EMAIL_RE = re.compile(r'^[^@\s]+@([^@\s]+\.[^@\s]+)$')

# def load_records(path: str) -> list[dict]:
#     """Load student records from a CSV file.
#     Args:
#         path: Path to the records CSV.
#     Returns:
#         A list of row dictionaries.
#     """

#     records, malformed = [], []
#     domain_counts, month_counts = Counter(), Counter()
#     by_domain = defaultdict(list)

#     with open(path, newline="") as f:
#         for row in csv.DictReader(f):
#             roll = row["roll"].strip()
#             email = row["email"].strip()

#             m = EMAIL_RE.match(email)
#             domain = m.group(1).lower() if m else None
#             if domain:
#                 domain_counts[domain] += 1
#             else:
#                 malformed.append((roll, email))

#             name = " ".join(row["name"].split()).title()

#             enrolled = None
#             try:
#                 enrolled = datetime.strptime(row["enrolled"].strip(), "%d-%m-%Y")
#                 month_counts[enrolled.strftime("%Y-%m")] += 1
#             except ValueError:
#                 pass

#             exam1_raw = row["exam1"].strip()
#             exam2_raw = row["exam2"].strip()
#             exam3_raw = row["exam3"].strip()
#             exam4_raw = row["exam4"].strip()

#             exam1 = int(exam1_raw) if exam1_raw else None
#             exam2 = int(exam2_raw) if exam2_raw else None
#             exam3 = int(exam3_raw) if exam3_raw else None
#             exam4 = int(exam4_raw) if exam4_raw else None
#             rec = {
#         "roll": roll,
#         "name": name,
#         "email": email,
#         "domain": domain,
#         "enrolled": enrolled,
#         "exam1": exam1,
#         "exam2": exam2,
#         "exam3": exam3,
#         "exam4": exam4,
# }
#             records.append(rec)
#             if domain:
#                 by_domain[domain].append(name)

#     return {
#         "records": records,
#         "domain_counts": domain_counts,
#         "malformed_emails": malformed,
#         "enrolments_per_month": month_counts,
#         "students_by_domain": by_domain,
#     }

# data = load_records("records.csv")

# print(data["domain_counts"])
# print(data["malformed_emails"])
# print(data["enrolments_per_month"])
# print(data["students_by_domain"])


import csv
import re
from collections import Counter, defaultdict
from datetime import datetime

EMAIL_RE = re.compile(r"^[^@\s]+@([^@\s]+\.[^@\s]+)$")


def parse_mark(value: str) -> int | None:
    """Convert a mark to an integer or None if blank."""
    value = value.strip()
    return int(value) if value else None


def normalize_name(name: str) -> str:
    """Return a cleaned, title-cased student name."""
    return " ".join(name.split()).title()


def parse_date(date: str) -> datetime | None:
    """Convert a date string into a datetime object."""
    try:
        return datetime.strptime(date.strip(), "%d-%m-%Y")
    except ValueError:
        return None


def extract_domain(email: str) -> str | None:
    """Extract the email domain if the email is valid."""
    match = EMAIL_RE.match(email.strip())
    if match:
        return match.group(1).lower()
    return None


def load_records(path: str) -> dict:
    """Load and clean student records from a CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        Dictionary containing cleaned records and summary statistics.
    """

    records = []
    malformed = []
    domain_counts = Counter()
    month_counts = Counter()
    by_domain = defaultdict(list)

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            roll = row["roll"].strip()
            email = row["email"].strip()

            domain = extract_domain(email)

            if domain:
                domain_counts[domain] += 1
            else:
                malformed.append((roll, email))

            name = normalize_name(row["name"])

            enrolled = parse_date(row["enrolled"])

            if enrolled:
                month_counts[enrolled.strftime("%Y-%m")] += 1

            rec = {
                "roll": roll,
                "name": name,
                "email": email,
                "domain": domain,
                "enrolled": enrolled,
                "exam1": parse_mark(row["exam1"]),
                "exam2": parse_mark(row["exam2"]),
                "exam3": parse_mark(row["exam3"]),
                "exam4": parse_mark(row["exam4"]),
            }

            records.append(rec)

            if domain:
                by_domain[domain].append(name)

    return {
        "records": records,
        "domain_counts": domain_counts,
        "malformed_emails": malformed,
        "enrolments_per_month": month_counts,
        "students_by_domain": by_domain,
    }


data = load_records("records.csv")

print(data["domain_counts"])
print(data["malformed_emails"])
print(data["enrolments_per_month"])
print(data["students_by_domain"])
