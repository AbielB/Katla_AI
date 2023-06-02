# Read the words from 5letter_new.txt
with open('5letter_new.txt', 'r') as file:
    valid_words = set(word.strip() for word in file)

# Filter words from wordle_indonesia.txt
filtered_words = []
with open('wordle_indonesia.txt', 'r') as file:
    for word in file:
        word = word.strip()
        if word in valid_words:
            filtered_words.append(word)

# Write the filtered words to a new file
with open('wordle_indonesia_new.txt', 'w') as file:
    file.write('\n'.join(filtered_words))
