import re

with open("email.txt", "r") as file:
    text = file.read()

print("File content:\n", text)

email_regex = r'(?<!\S)([a-zA-Z0-9._%+-]+(?:[.-][a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?!\S)'

def extract_emails(text):
    found_emails = re.findall(email_regex, text)
    return found_emails

def clean_emails(email_list):
    cleaned = []
    for email in email_list:
        print("Checking email:", email)
        if email.endswith(".com") or email.endswith(".org"):
            cleaned.append(email.lower())
    return cleaned

emails = extract_emails(text)

cleaned_emails = clean_emails(emails)

print("Raw emails found:", emails)
print("Cleaned emails:", cleaned_emails)

modified_text = re.sub(email_regex, '[EMAIL]', text)

print("\nModified text (emails replaced with [EMAIL]):")
print(modified_text)

domain_counts = {}
for email in cleaned_emails:
    domain = email.split('@')[1]
    print("Extracted domain:", domain)
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

print("\nDomain counts:")
for domain, count in domain_counts.items():
    print(f"{domain}: {count}")
