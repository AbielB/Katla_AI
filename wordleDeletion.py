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
            if guess_letters[:i].count(guess_letter) <= final_letters.count(guess_letter):
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

def delete_word_from_file(word):
    # Open the file in read mode
    with open('wordle_indonesia.txt', 'r') as file:
        lines = file.readlines()

    # Open the file in write mode
    with open('wordle_indonesia.txt', 'w') as file:
        for line in lines:
            # Write all lines except the line containing the word to delete
            if line.strip() != word:
                file.write(line)

# Example usage:
guess_array = ['kiran','tarik','kurai','sarik','kerai','kiras','katir','kitar','tiran','kuran']
for guess_words in guess_array:
    guess_word = guess_words
    total_tries = 0
    total_loop = 0
    lost_count = 0
    with open('wordle_indonesia.txt', 'r') as file:
        final_arr = [line.strip() for line in file]
    for final_word in final_arr:
        with open('5letter_indo.txt', 'r') as file:
            eligible_words = [line.strip() for line in file]
        loop_count = 0
        while True:
            loop_count += 1
            combination = wordle_result(guess_word, final_word)

            if combination == 'ggggg':
                print(guess_words," -> ",final_word)
                break

            top_entropy_words = find_top_entropy_words(guess_word, combination)

            if not top_entropy_words:
                print("Kombinasi tidak ditemukan: ",final_word)
                delete_word_from_file(final_word)
                break
            else:
                # Print the top 10 eligible words with their entropy scores
                for word, entropy_total in top_entropy_words:
                    guess_word = word

        print(f"Total loops: {loop_count}")
        if loop_count > 6: 
            lost_count += 1
            print("lost")
        total_loop += loop_count
        total_tries += 1

    avg_loop = total_loop/total_tries
    print("avg tries ",guess_word," = ",avg_loop)
    print ("lost count ",guess_word," = ",lost_count)
    #insert result to wordleSimulation.txt
    with open('wordleSimulation.txt', 'a') as file:
        file.write(f"{guess_word}: {avg_loop}\n")
        #and lost count
        file.write(f"{guess_word}: {lost_count}\n")
