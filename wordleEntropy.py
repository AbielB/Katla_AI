import math

def wordle_result(guess_word, final_word):
    result = []
    guess_letters = list(guess_word)
    final_letters = list(final_word)

    # Iterate through each letter in the guess word
    for i in range(len(guess_word)):
        guess_letter = guess_letters[i]

        if guess_letter == final_letters[i]:
            result.append('G')  # Letter in the same place as the result
        elif guess_letter in final_letters:
            if guess_letters[:i].count(guess_letter) < final_letters.count(guess_letter):
                result.append('Y')  # Letter appears in a different place
            else:
                result.append('-')  # Letter appears more in the guess word, mark as '-'
        else:
            result.append('-')  # Letter not in the final word

    return result

# Open the wordle_indonesia.txt file
with open('wordle_indonesia.txt', 'r') as file:
    word_scores = []

    for guess_word in file:
        guess_word = guess_word.strip()
        results_count = {}
        total_count = 0

        # Open the wordle_indonesia.txt file again to process each final word
        with open('wordle_indonesia.txt', 'r') as inner_file:
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
            log_probability = math.log(1 / probability)
            entropy = probability * log_probability
            entropy_total += entropy

        word_scores.append((guess_word, entropy_total))

    # Sort the word scores in descending order based on entropy_total
    word_scores.sort(key=lambda x: x[1], reverse=True)

    # Print the top 10 words with the highest entropy_total
    for word, entropy_total in word_scores[:10]:
        print(f'{word}: {entropy_total}')


#tarik: 4.208741141242601
#tikar: 4.150048185662924
#sakit: 4.146190398481941
#kuras: 4.130723017353524
#rakit: 4.121300570009099
#tukar: 4.119299205592329
#surat: 4.117283905852258
#sikat: 4.116594488833842
#sukar: 4.114549820621672
#sukat: 4.103920462358214