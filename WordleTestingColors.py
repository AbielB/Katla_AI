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

guess_word = input("masukkan guess word: ")
final_word = input("masukkan final word: ")
answer = wordle_result(guess_word, final_word)
print(answer)