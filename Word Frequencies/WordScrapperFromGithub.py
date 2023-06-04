import urllib.request
import re
import time

# Define the regular expression pattern to match 5-letter words consisting of letters only
pattern = re.compile(r'^[a-zA-Z]{5}$')

# List to store the 5-letter words
kosakata = []

# Loop through each letter of the alphabet
for i in 'abcdefghijklmnopqrstuvwxyz':
    url = "https://raw.githubusercontent.com/bekicot/indonesian_words/master/words/{}".format(i)
    txt_file = urllib.request.urlopen(url)
    time.sleep(1)

    for line in txt_file:
        kata = line.decode("utf-8").strip()
        if pattern.match(kata):
            kosakata.append(kata)

# Write the 5-letter words to a text file
with open('all_words_indo_new.txt', 'w') as file:
    for word in kosakata:
        file.write(word + '\n')
