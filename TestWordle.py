import math

# Load wordlist
with open("wordle.txt") as f:
    wordlist = [word.strip() for word in f.readlines()]

# Define function to calculate entropy
def calculate_entropy(guess_word, guesses, wordlist):
    freq_dict = {}
    for word in wordlist:
        for i, (letter, color) in enumerate(guesses):
            if color == 'G' and letter != word[i]:
                break
            if color == 'Y' and letter not in word:
                break
        else:
            if word != guess_word:
                freq_dict[word] = freq_dict.get(word, 0) + 1
    N = sum(freq_dict.values())
    entropy = - (1/N) * math.log2(1/N)
    return entropy, freq_dict

# Get user's guess word and color guesses
guess_word = input("Enter your guess word: ")
guesses = []
for i in range(len(guess_word)):
    letter = guess_word[i]
    color = input(f"Enter the color for the {i+1}th letter (G/Y/-): ")
    guesses.append((letter, color))

# Calculate entropy of guess word and get possible answers
entropy, freq_dict = calculate_entropy(guess_word, guesses, wordlist)
possible_answers = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)

# Output entropy and possible answers
print(f"Entropy of {guess_word} based on the given guesses: {entropy}")
print(f"Possible answers: {', '.join(possible_answers)}")
