import re

# Load the possible words from wordle.txt file
with open('indonesian-words.txt', 'r') as f:
    words = f.read().splitlines()

# Filter words with non-letter characters
words = [word for word in words if re.match(r'^[a-zA-Z]+$', word) and len(word) == 5]

# Write filtered words to a new file
with open('wordle_indonesia.txt', 'w') as f:
    f.write('\n'.join(words))
