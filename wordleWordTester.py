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
    return word_scores[:1]


# Example usage:
total_tries = 0
total_loop = 0
lost_count = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

best_words = input("masukkan kata 5 huruf: ")
with open('5letter_indo.txt', 'r') as file:
    final_arr = [line.strip() for line in file]

total_count = 0
for final_word in final_arr:
    total_count += 1
    guess_word = best_words
    loop_count = 0
    with open('5letter_indo.txt', 'r') as file:
        eligible_words = [line.strip() for line in file]

    while True:
        loop_count += 1
        combination = wordle_result(guess_word, final_word)

        if combination == 'ggggg':
            print(best_words, " -> ", final_word)
            break

        top_entropy_words = find_top_entropy_words(guess_word, combination)

        if not top_entropy_words:
            print("Kombinasi tidak ditemukan: ", final_word)
            break
        else:
            for word, entropy_total in top_entropy_words:
                guess_word = word

    print(f"Total loops: {loop_count}")
    if loop_count == 1:
        count_1 += 1
    if loop_count == 2:
        count_2 += 1
    if loop_count == 3:
        count_3 += 1
    if loop_count == 4:
        count_4 += 1
    if loop_count == 5:
        count_5 += 1
    if loop_count == 6:
        count_6 += 1
    if loop_count > 6:
        lost_count += 1
        print("lost")
    total_loop += loop_count
    total_tries += 1

win_rate = 1-(lost_count/total_count)
avg_loop = total_loop/total_tries
print(best_words, " = ", avg_loop)
print("lost = ", lost_count )
print("win rate = ", win_rate)
print("1st try = ", count_1)
print("2nd try = ", count_2)
print("3rd try = ", count_3)
print("4th try = ", count_4)
print("5th try = ", count_5)
print("6th try = ", count_6)
print("jumlah kata = ",total_count)