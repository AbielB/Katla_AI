# Read the contents of wordle_indonesia.txt
with open('katla_indonesia.txt', 'r') as file:
    wordle_contents = set(line.strip() for line in file)

# Read the contents of jawaban.txt
with open('all_words_indo_new.txt', 'r') as file:
    jawaban_contents = set(line.strip().lower() for line in file)

# Combine the contents without duplicates
combined_contents = wordle_contents.union(jawaban_contents)

# Write the combined contents to katla_indonesia.txt
with open('katla_wordfreq.txt', 'w') as file:
    for line in combined_contents:
        file.write(line + '\n')

print("Combination completed. Result saved to katla_indonesia.txt.")
