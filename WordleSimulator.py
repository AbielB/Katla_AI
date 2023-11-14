import math

eligible_words = []

def wordle_result(guess_word, final_word):
    result = []
    guess_letters = list(guess_word)
    final_letters = list(final_word)

    # Iterate through each letter in the guess word
    already_yellow = []
    for i in range(len(guess_word)):
        guess_letter = guess_letters[i]

        if guess_letter == final_letters[i]:
            result.append('g')  # Letter in the same place as the result
        elif guess_letter in final_letters:
            match_found = True

            count_guess = guess_letters.count(guess_letter)
            count_final = final_letters.count(guess_letter)
            for y in range(len(final_letters)):
                if final_letters[y] == guess_letter and guess_letters[y] != guess_letter:
                    if guess_letter in already_yellow and count_guess > count_final:
                        match_found = True
                        break
                    else:
                        result.append('y')  # Letter appears more in the guess word, mark as '-'
                        already_yellow.append(guess_letter)
                        match_found = False
                        break
            if match_found:
                result.append('-')  # Letter appears in a different place
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
        entropy = probability * math.log2(1/probability)
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
    eligible_count = 0

    for word in eligible_words:
        eligible_count += 1
        entropy_total = calculate_entropy(word)
        word_scores.append((word, entropy_total))

    # Sort the word scores in descending order based on entropy_total
    word_scores.sort(key=lambda x: x[1], reverse=True)

    # Return the top 10 eligible words with their entropy scores and updated eligible_words
    return word_scores[:10], eligible_count


# Example usage:
with open('5letter_indo.txt', 'r') as file:
    eligible_words = [line.strip() for line in file]
    all_words = [line.strip() for line in file]

loop_count = 0

while True:
    loop_count += 1
    guess_word = input("Masukkan kata tebakan: ")
    combination = input("Masukkan kombinasi warna: ")

    if combination == 'ggggg':
        print("You win!")
        break

    top_entropy_words = find_top_entropy_words(guess_word, combination)

    if not top_entropy_words[0]:
        print("Kombinasi tidak ditemukan.")
        break
    else:
        # Print the top 10 eligible words with their entropy scores
        print('jumlah eligible = ',top_entropy_words[1])
        for word, entropy_total in top_entropy_words[0]:
            print(f'{word}: {entropy_total}')

    print()  # Add a new line for separation

print(f"Jumlah Percobaan: {loop_count}")