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
    return word_scores[:1]


# Example usage:
guess_array = ['tarik','tikar','sakit','kuras','rakit','tukar','surat','sikat','sukar','sukat']

for best_words in guess_array:
    total_tries = 0
    total_loop = 0
    lost_count = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0

    with open('wordle_indonesia.txt', 'r') as file:
        final_arr = [line.strip() for line in file]

    for final_word in final_arr:
        guess_word = best_words
        loop_count = 0
        with open('wordle_indonesia.txt', 'r') as file:
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

    avg_loop = total_loop/total_tries
    print(best_words, " = ", avg_loop)
    print("lost = ", lost_count)

    win_rate = 1-(lost_count/1473)
    with open('wordleSimulation.txt', 'a') as file:
        file.write(f"{best_words}: {avg_loop}\n")
        file.write(f"lost: {lost_count}\n")
        file.write(f"win rate: {win_rate}\n")
        file.write(f"1st try: {count_1}\n")
        file.write(f"2nd try: {count_2}\n")
        file.write(f"3rd try: {count_3}\n")
        file.write(f"4th try: {count_4}\n")
        file.write(f"5th try: {count_5}\n")
        file.write(f"6th try: {count_6}\n")

# tarik: 4.208741141242601
# tikar: 4.150048185662924
# sakit: 4.146190398481941
# kuras: 4.130723017353524
# rakit: 4.121300570009099
# tukar: 4.119299205592329
# surat: 4.117283905852258
# sikat: 4.116594488833842
# sukar: 4.114549820621672
# sukat: 4.103920462358214