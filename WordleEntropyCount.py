import math

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

# Open the wordle_indonesia.txt file
with open('wordle_indonesia.txt', 'r') as file:
    word_scores = []
    guess_word = input("Masukkan kata untuk cek entropi: ")
    combination = input("masukkan kombinasi: ")
    results_count = {}
    total_count = 0

    # Open the wordle_indonesia.txt file again to process each final word
    with open('5letter_indo.txt', 'r') as inner_file:
        for line in inner_file:
            final_word = line.strip()
            result = wordle_result(guess_word, final_word)

            # Update the count for each result array
            if result in results_count:
                results_count[result] += 1
            else:
                results_count[result] = 1

            total_count += 1

    entropy_total = 0

    # Calculate the probability multiplied by log(1/probability) for each result array
    for result, count in results_count.items():
        if result == combination:
            print(count)
            print(total_count)
            probability = count / total_count
            print("probability = ", probability)
            print("1 / probability = ", 1/probability)
            log_probability = math.log2(1 / probability)
            print("information = ", log_probability)
            entropy = probability * log_probability
            entropy_total += entropy

    word_scores.append((guess_word, entropy_total))

    # Sort the word scores in descending order based on entropy_total
    word_scores.sort(key=lambda x: x[1], reverse=True)

    # Print the top 10 words with the highest entropy_total
    for word, entropy_total in word_scores[:10]:
        print(f'{word}: {entropy_total}')
