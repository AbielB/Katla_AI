# Open the input file for reading
with open('AllWordIndo.txt', 'r') as input_file:
    # Open the output file for writing
    with open('5letter_new.txt', 'w') as output_file:
        # Iterate over each line in the input file
        for line in input_file:
            # Remove leading/trailing whitespaces and split the line into words
            words = line.strip().split()

            # Iterate over each word in the line
            for word in words:
                # Check if the word has exactly 5 letters
                if len(word) == 5:
                    # Write the word to the output file
                    output_file.write(word + '\n')
