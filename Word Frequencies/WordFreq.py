input_file = "id50k.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as file:
    with open(output_file, "w", encoding="utf-8") as output:
        for line in file:
            word, number = line.strip().split()

            if len(word) == 5:
                output.write(f"{word} {number}\n")

print("Extraction complete. The words of length 5 and their numbers have been written to the output file.")
