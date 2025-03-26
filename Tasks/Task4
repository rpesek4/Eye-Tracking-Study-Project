import re

with open("transactions.txt", "r") as file:
    text = file.read()

card_regex = r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\b'

def extract_card_numbers(text):
    """Finds all credit card numbers in text."""
    return re.findall(card_regex, text)

def mask_card_numbers(text):
    """Masks credit card numbers, showing only the last 4 digits."""
    return re.sub(card_regex, lambda m: '*' * (len(m.group()) - 4) + m.group()[-4:], text)

found_cards = extract_card_numbers(text)

modified_text = mask_card_numbers(text)

print("Extracted Card Numbers:", found_cards)

print("\nModified text (masked credit card numbers):")
print(modified_text)

issuer_counts = {"Visa": 0, "MasterCard": 0, "Amex": 0, "Discover": 0}

for card in found_cards:
    if re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", card):
        issuer_counts["Visa"] += 1
    elif re.match(r"^5[1-5][0-9]{14}$", card):
        issuer_counts["MasterCard"] += 1
    elif re.match(r"^3[47][0-9]{13}$", card):
        issuer_counts["Amex"] += 1
    elif re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", card):
        issuer_counts["Discover"] += 1

print("\nCard Issuer Counts:")
for issuer, count in issuer_counts.items():
    if count > 0:
        print(f"{issuer}: {count}")
