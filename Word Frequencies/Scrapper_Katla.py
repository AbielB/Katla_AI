import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome driver
driver = webdriver.Chrome()

# Loop 100 times
for _ in range(200):
    # Navigate to the website
    driver.get('https://www.wordlegame.org/id')


    # Click the divs 'm', 'o', 'b', 'i', 'l'
    letters = ['m', 'o', 'b', 'i', 'l']
    for letter in letters:
        divs = driver.find_elements(By.XPATH, f"//div[@class='Game-keyboard-button' and text()='{letter}']")
        for div in divs:
            div.click()

    # Press the "Enter" key
    div.send_keys(Keys.ENTER)


    # Click the "give_up" button
    give_up_button = driver.find_element(By.CLASS_NAME, 'give_up')
    give_up_button.click()

    # Wait for 3 seconds
    time.sleep(1)

    # Wait for the word to appear
    word_element = driver.find_element(By.CSS_SELECTOR, 'div.word span')
    word = word_element.text.lower()

    # Read the existing words from jawaban.txt
    existing_words = []
    try:
        with open('jawaban.txt', 'r') as file:
            existing_words = file.read().splitlines()
    except FileNotFoundError:
        pass

    # Check if the word is a duplicate
    if word not in existing_words:
        # Store the lowercase word in the text file
        with open('jawaban.txt', 'a') as file:
            file.write(word + '\n')

        print(f"Word '{word}' has been extracted and saved to jawaban.txt.")
    else:
        print(f"Duplicate word '{word}' found. Skipping...")

# Close the browser
driver.quit()
