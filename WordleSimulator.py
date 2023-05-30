import math

eligible_words = []

def wordle_result(guess_word, final_word):
    result = []
    guess_letters = list(guess_word)
    final_letters = list(final_word)

    # Iterate through each letter in the guess word
    for i in range(len(guess_word)):
        guess_letter = guess_letters[i]

        if guess_letter == final_letters[i]:
            result.append('g')  # Letter in the same place as the result
        elif guess_letter in final_letters:
            if guess_letters[:i].count(guess_letter) < final_letters.count(guess_letter):
                result.append('y')  # Letter appears in a different place
            else:
                result.append('-')  # Letter appears more in the guess word, mark as '-'
        else:
            result.append('-')  # Letter not in the final word

    # Turn result into a string
    result = ''.join(result)
    return result


def calculate_entropy(guess_word):
    results_count = {}
    total_count = len(eligible_words)

    for final_word in eligible_words:
        result = wordle_result(guess_word, final_word)

        if result in results_count:
            results_count[result] += 1
        else:
            results_count[result] = 1

    entropy_total = 0

    for result, count in results_count.items():
        probability = count / total_count
        entropy = -probability * math.log2(probability)
        entropy_total += entropy

    return entropy_total


def find_top_entropy_words(guess_word, combination):
    new_eligible = []

    for final_word in eligible_words:
        result = wordle_result(guess_word, final_word)

        # Update the count for each result array
        if result == combination:
            # Insert into new_eligible
            new_eligible.append(final_word)

    # Clear eligible_words and replace it with new_eligible
    eligible_words.clear()
    eligible_words.extend(new_eligible)

    word_scores = []

    for word in eligible_words:
        entropy_total = calculate_entropy(word)
        word_scores.append((word, entropy_total))

    # Sort the word scores in descending order based on entropy_total
    word_scores.sort(key=lambda x: x[1], reverse=True)

    # Return the top 10 eligible words with their entropy scores and updated eligible_words
    return word_scores[:5]


# Example usage:
with open('5letter_new.txt', 'r') as file:
    eligible_words = [line.strip() for line in file]

loop_count = 0

while True:
    loop_count += 1
    guess_word = input("Masukkan kata tebakan: ")
    combination = input("Masukkan kombinasi warna: ")

    if combination == 'ggggg':
        print("You win!")
        break

    top_entropy_words = find_top_entropy_words(guess_word, combination)

    if not top_entropy_words:
        print("Kombinasi tidak ditemukan.")
        break
    else:
        # Print the top 10 eligible words with their entropy scores
        for word, entropy_total in top_entropy_words:
            print(f'{word}: {entropy_total}')

    print()  # Add a new line for separation

print(f"Jumlah Percobaan: {loop_count}")