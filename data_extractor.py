import re

# Load sample input text
with open("sample_input.txt", "r") as file:
    text = file.read()

# Regex patterns
patterns = {
    "Emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    "URLs": r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?',
    "Phone Numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "Credit Card Numbers": r'\b(?:\d{4}[- ]?){3}\d{4}\b',
    "Time (12/24 Hour)": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
}

# Edge case inputs to test against
edge_cases = {
    "Test Email": "user@@example..com",
    "Test URL": "htp:/wrong.url",
    "Test Phone": "1234567",
    "Test Time": "25:99",
    "Second Test Email": "test.email@domain.com",
    "Second Test Phone": "321.654.0987",
    "Second Test Time": "23:45"
}

# Open output file
with open("output.txt", "w") as output_file:

    # Main extraction from sample input
    output_file.write("=== Extracted Matches from Sample Input ===\n")
    print("=== Extracted Matches from Sample Input ===\n")
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        output_file.write(f"\n{key}:\n")
        print(f"{key}:")
        if matches:
            for match in matches:
                output_file.write(f" - {match}\n")
                print(f" - {match}")
        else:
            output_file.write(" - No matches found.\n")
            print(" - No matches found.")
        print()

    # Edge case testing
    output_file.write("\n\n=== Edge Case Test Results ===\n")
    print("\n=== Edge Case Test Results ===\n")
    for case_label, case_text in edge_cases.items():
        output_file.write(f"\nTesting: {case_label}\n")
        print(f"Testing: {case_label}")
        for key, pattern in patterns.items():
            matches = re.findall(pattern, case_text)
            if matches:
                output_file.write(f"[{key}] Match: {matches}\n")
                print(f"[{key}] Match: {matches}")
            else:
                output_file.write(f"[{key}] No match\n")
                print(f"[{key}] No match")
        print()
