import math

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
            match_found = True
            for y in range(len(final_letters)):
                if final_letters[y] == guess_letter and guess_letters[y] != guess_letter:
                    result.append('y')  # Letter appears more in the guess word, mark as '-'
                    match_found = False
                    break
            if match_found:
                result.append('-')  # Letter appears in a different place
        else:
            result.append('-')  # Letter not in the final word

    return result

word_scores = []  # Initialize the word_scores list outside the loop

with open('5letter_indo.txt', 'r') as file:
    for newline in file:
        guess_word = newline.strip()
        results_count = {}
        total_count = 0

        # Open the WordlePossibleAnswer_en.txt file again to process each final word
        with open('5letter_indo.txt', 'r') as inner_file:
            for line in inner_file:
                final_word = line.strip()
                result = tuple(wordle_result(guess_word, final_word))

                # Update the count for each result array
                if result in results_count:
                    results_count[result] += 1
                else:
                    results_count[result] = 1

                total_count += 1

        entropy_total = 0

        # Calculate the probability multiplied by log(1/probability) for each result array
        for result, count in results_count.items():
            probability = count / total_count
            log_probability = math.log2(1 / probability)
            entropy = probability * log_probability
            entropy_total += entropy

        word_scores.append((guess_word, entropy_total))

    # Sort the word scores in descending order based on entropy_total
    word_scores.sort(key=lambda x: x[1], reverse=True)

    # Print the top 10 words with the highest entropy_total
    for word, entropy_total in word_scores[:10]:
        print(f'{word}: {entropy_total}')
