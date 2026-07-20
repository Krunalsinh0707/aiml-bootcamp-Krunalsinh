import re
from collections import Counter, defaultdict
from datetime import datetime
import re

level_counts = Counter()
hour_counts = Counter()
error_messages = Counter()
log_by_level = defaultdict(list)


pattern = r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(INFO|WARN|ERROR)\s+(.*)$'




with open("sample_application.log", "r") as file:
    for line in file:
        match = re.match(pattern, line.strip())
        if match:
            timestamp, level, message = match.groups()
            timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            level_counts[level] += 1
            hour_counts[timestamp.hour] += 1
            log_by_level[level].append((timestamp, message))

            print(f"Timestamp: {timestamp}")
            print(f"Level: {level}")
            print(f"Message: {message}")
            print("-" * 40)
        if level == "ERROR":
           error_messages[message] += 1

for level, entries in log_by_level.items():
    print(f"\n{level}:")
    for timestamp, message in entries:
        print(timestamp, "-", message)

        
busiest_hour, count = hour_counts.most_common(1)[0]
most_common_error, count = error_messages.most_common(1)[0]


print("\nEntries per level:")
for level, count in level_counts.items():
    print(f"{level}: {count}")

print(f"\nMost Frequent ERROR Message: '{most_common_error}' ({count} times)")

print(f"\nBusiest Hour: {busiest_hour:02d}:00 with {count} entries")