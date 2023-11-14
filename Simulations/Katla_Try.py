import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the website
driver.get('https://www.wordlegame.org/id')

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
total_loop = 0
total_tries = 0
lost = 0

# Loop until a break condition is met
for tries in range(100):
    is_lost = False
    with open('5letter_indo.txt', 'r') as file:
        eligible_words = [line.strip() for line in file]
    # Reset the turn counter and guess word
    turn = 0
    guess_word = 'kiras'
    print("New Game!")

    try:
        # Loop 200 times
        for _ in range(7):
            combination = []
            for letter in guess_word:
                divs = driver.find_elements(By.XPATH, f"//div[contains(@class, 'Game-keyboard-button') and text()='{letter}']")
                for div in divs:
                    div.click()

            # Press the "Enter" key
            div.send_keys(Keys.ENTER)
            time.sleep(1)

            row_elements = driver.find_elements(By.CSS_SELECTOR, '.Row.Row-locked-in')
            while len(row_elements) != turn+1:
                print("kata tidak ditemukan")
                for _ in range(5):
                    div.send_keys(Keys.BACKSPACE)
                i = 0
                if turn == 0:
                    #rewrite
                    for letter in guess_word:
                        divs = driver.find_elements(By.XPATH, f"//div[contains(@class, 'Game-keyboard-button') and text()='{letter}']")
                        for div in divs:
                            div.click()
                    # Press the "Enter" key
                    div.send_keys(Keys.ENTER)
                    time.sleep(1)
                    break
                next_word_found = True
                while i < len(top_entropy_words[0]) and len(row_elements) != turn+1:
                    print('amount of reserve words = ', len(top_entropy_words[0]))
                    guess_word = top_entropy_words[0][i][0]
                    print(guess_word)
                    time.sleep(1)
                    for _ in range(5):
                        div.send_keys(Keys.BACKSPACE)
                    for letter in guess_word:
                        divs = driver.find_elements(By.XPATH,f"//div[contains(@class, 'Game-keyboard-button') and text()='{letter}']")
                        for div in divs:
                            div.click()
                    div.send_keys(Keys.ENTER)
                    i = i+1
                    time.sleep(1)
                    row_elements = driver.find_elements(By.CSS_SELECTOR, '.Row.Row-locked-in')
                    print('i = ', i )
                if len(row_elements) != turn + 1 :
                    is_lost = True
                    break

                row_elements = driver.find_elements(By.CSS_SELECTOR, '.Row.Row-locked-in')
            #check if is lost, then break
            if is_lost:
                print("Kombinasi tidak ditemukan.")
                driver.find_element(By.CLASS_NAME, 'give_up').click()
                div.send_keys(Keys.ENTER)
                break
            this_elements = row_elements[turn]
            # Find all div elements inside the current row element with class "Row-letter"
            letter_elements = this_elements.find_elements(By.CSS_SELECTOR, '.Row-letter')

            # Iterate over the letter elements
            for letter_element in letter_elements:
                # Get the class name of the letter element
                class_name = letter_element.get_attribute('class')

                # Extract the type of Row-letter
                row_letter_type = class_name.split(' ')[1]  # Assuming the second class represents the type

                # Extract the type of Row-letter
                if 'letter-absent' in class_name:
                    combination.append('-')
                elif 'letter-elsewhere' in class_name:
                    combination.append('y')
                elif 'letter-correct' in class_name:
                    combination.append('g')

            combination_string = ''.join(combination)
            if combination_string == 'ggggg':
                break
            if combination_string != 'ggggg' and turn == 5 :
                is_lost = True
            top_entropy_words = find_top_entropy_words(guess_word, combination_string)
            # Print the combination string
            print(combination_string)

            if not top_entropy_words[0]:
                print("Kombinasi tidak ditemukan.")
                driver.find_element(By.CLASS_NAME, 'give_up').click()
                div.send_keys(Keys.ENTER)
                is_lost = True
                break
            else:
                # Print the top 10 eligible words with their entropy scores
                print('jumlah eligible = ', top_entropy_words[1])
                #print all eligible words
                for word, entropy_total in top_entropy_words[0]:
                     print(f'{word}')
                for word, entropy_total in top_entropy_words[0]:
                    guess_word = word

            turn += 1

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Restarting the loop...")

    # Press Enter to start the loop again

    loop_count = turn + 1
    print('loops = ', loop_count)
    if loop_count == 1 and not is_lost:
        count_1 += 1
    if loop_count == 2 and not is_lost:
        count_2 += 1
    if loop_count == 3 and not is_lost:
        count_3 += 1
    if loop_count == 4 and not is_lost:
        count_4 += 1
    if loop_count == 5 and not is_lost:
        count_5 += 1
    if loop_count == 6 and not is_lost:
        count_6 += 1
    if is_lost:
        print("Lost")
        lost += 1
    total_loop += loop_count
    total_tries += 1
    time.sleep(1)
    div.send_keys(Keys.ENTER)
    time.sleep(1)
    div.send_keys(Keys.ENTER)
    time.sleep(1)


avg_loop = total_loop/total_tries
print("Tarik Average loop count = ", avg_loop)
print("lost = ", lost)

win_rate = 1-(lost/total_tries)
with open('wordleSimulation.txt', 'a') as file:
    file.write(f"lost: {lost}\n")
    file.write(f"Avg Loop: {avg_loop}\n")
    file.write(f"win rate: {win_rate}\n")
    file.write(f"1st try: {count_1}\n")
    file.write(f"2nd try: {count_2}\n")
    file.write(f"3rd try: {count_3}\n")
    file.write(f"4th try: {count_4}\n")
    file.write(f"5th try: {count_5}\n")
    file.write(f"6th try: {count_6}\n")


# Close the browser
driver.quit()