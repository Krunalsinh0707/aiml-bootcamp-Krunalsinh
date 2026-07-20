import re
from collections import Counter

text = '''
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these
'''

# Email regex
emails = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", text)

# Indian mobile numbers
phone_pattern = r'(?:\+91[- ]?|91[- ]?)?[6-9]\d{4}[- ]?\d{5}'

phone_numbers = re.findall(phone_pattern, text)

email_pattern = r'([\w.+-]+)@([\w-]+(?:\.[\w-]+)+)'

emails = re.findall(email_pattern, text)


domain_counts = Counter(domain for _, domain in emails)


print("Emails found:")
for e in emails:
    print(" ", e)

print("\nPhone numbers found:")
print(phone_numbers)



print("\nUsername\tDomain")
for username, domain in emails:
    print(username, "\t", domain)


print("\nEmails per domain:")
for domain, count in domain_counts.items():
    print(f"{domain}: {count}")