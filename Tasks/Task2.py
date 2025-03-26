import re

text = """
The project started on 12-03-2021 and ended on 20-05-2022.
There was a meeting on 15-06-2022, and another on 05-11-2022.
Final reports were due by 01-12-2022.
"""

date_pattern = r'\b(\d{2})-(\d{2})-(\d{4})\b'

def convert_date_format(match):
    day, month, year = match.groups()
    return f"{year}-{month}-{day}"

dates = re.findall(date_pattern, text)

print("Original dates and converted dates:")
for date in dates:
    original_date = f"{date[0]}-{date[1]}-{date[2]}"
    converted_date = convert_date_format(re.match(date_pattern, original_date))
    print(f"Original: {original_date} -> Converted: {converted_date}")

modified_text = re.sub(date_pattern, convert_date_format, text)

print("\nModified text:")
print(modified_text)
