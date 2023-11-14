input_file_path = "5letter_indo.txt"
output_file_path = "5letter_toJS.txt"

with open(input_file_path, "r") as input_file:
    words = input_file.read().splitlines()

quoted_comma_words = ['"' + word + '",' for word in words]

with open(output_file_path, "w") as output_file:
    output_file.write("\n".join(quoted_comma_words))

print("Quotes and commas added to words and saved in output.txt")
