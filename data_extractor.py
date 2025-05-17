import re

# Read from sample input
with open("sample_input.txt", "r") as file:
    text = file.read()

# Define regex patterns
patterns = {
    "Emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    "URLs": r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?',
    "Phone Numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "Credit Card Numbers": r'\b(?:\d{4}[- ]?){3}\d{4}\b',
    "Time (12/24 Hour)": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
}

# Extract and print results
for key, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"\n{key}:")
    for match in matches:
        print(f" - {match}")

# Write results to output file
with open("output.txt", "w") as file:
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        file.write(f"\n{key}:\n")
        for match in matches:
            file.write(f" - {match}\n")