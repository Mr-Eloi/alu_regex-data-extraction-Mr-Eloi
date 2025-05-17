import re

# Same regex patterns as in main script
test_data = {
    "Test Email": "user@@example..com",
    "Test URL": "htp:/wrong.url",
    "Test Phone": "1234567",
    "Test Time": "25:99",
}

patterns = {
    "Email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    "URL": r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?',
    "Phone": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "Time": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
}

print("Running Edge Case Tests:")
for label, text in test_data.items():
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            print(f"[{label}] Unexpected match in {name}: {matches}")
        else:
            print(f"[{label}] Passed for {name}")