import PyPDF2
import re

# Open the PDF file in binary mode
with open('kbbi.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Extract text from each page
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

# Combine lines ending with '-' with the next line
text = re.sub(r'-\n', '', text)

# Find all unique 5-letter words containing only letters and not preceded by '-'
words = set(re.findall(r'(?<!-)\b[a-zA-Z]{5}\b', text.lower()))

# Save the words to a file
with open('5letter_indo.txt', 'w') as file:
    file.writelines(word + '\n' for word in words)

print(f"Extracted {len(words)} unique 5-letter words. Saved to 5letter_indo.txt.")
