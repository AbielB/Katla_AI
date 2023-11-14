# Read the contents of the file
with open('katla_allwords.txt', 'r') as file:
    words = file.readlines()

# Sort the words alphabetically
words.sort()

# Write the sorted words back to the same file
with open('katla_allwords.txt', 'w') as file:
    file.writelines(words)
