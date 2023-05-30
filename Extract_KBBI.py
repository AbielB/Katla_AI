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

# Find all unique 5-letter words containing only letters
words = set(re.findall(r'\b[a-zA-Z]{5}\b', text.lower()))

# Save the words to a file
with open('5letter_indo.txt', 'w') as file:
    file.writelines(word + '\n' for word in words)
