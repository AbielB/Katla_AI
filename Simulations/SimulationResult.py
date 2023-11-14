result_file = "wordleSimulation.txt"

# Initialize variables to store combined statistics
total_lost = 0
total_avg_loop = 0
total_win_rate = 0
total_tries = 0
total_1st_try = 0
total_2nd_try = 0
total_3rd_try = 0
total_4th_try = 0
total_5th_try = 0
total_6th_try = 0
count = 0

# Read the text file
with open(result_file, 'r') as file:
    lines = file.readlines()

# Process each line in the text file
for line in lines:
    line = line.strip()

    # Check if it's a 'lost' line
    if line.startswith("lost:"):
        lost_count = int(line.split(":")[1])
        total_lost += lost_count

    # Check if it's an 'Avg Loop' line
    elif line.startswith("Avg Loop:"):
        avg_loop = float(line.split(":")[1])
        total_avg_loop += avg_loop

    # Check if it's a 'win rate' line
    elif line.startswith("win rate:"):
        win_rate = float(line.split(":")[1])
        total_win_rate += win_rate

    # Check if it's a '1st try' line
    elif line.startswith("1st try:"):
        count_1 = int(line.split(":")[1])
        total_1st_try += count_1

    # Check if it's a '2nd try' line
    elif line.startswith("2nd try:"):
        count_2 = int(line.split(":")[1])
        total_2nd_try += count_2

    # Check if it's a '3rd try' line
    elif line.startswith("3rd try:"):
        count_3 = int(line.split(":")[1])
        total_3rd_try += count_3

    # Check if it's a '4th try' line
    elif line.startswith("4th try:"):
        count_4 = int(line.split(":")[1])
        total_4th_try += count_4

    # Check if it's a '5th try' line
    elif line.startswith("5th try:"):
        count_5 = int(line.split(":")[1])
        total_5th_try += count_5

    # Check if it's a '6th try' line
    elif line.startswith("6th try:"):
        count_6 = int(line.split(":")[1])
        total_6th_try += count_6

    # Check if it's an empty line (indicates the end of a set of statistics)
    elif line == "":
        count += 1

# Calculate the average values
total_sets = count
average_lost = total_lost / total_sets
average_avg_loop = total_avg_loop / total_sets
average_win_rate = total_win_rate / total_sets

# Print the combined statistics
print("Combined Statistics sets : ", total_sets)
print("Total Lost:", total_lost)
print("Average Avg Loop:", average_avg_loop)
print("Average Win Rate:", average_win_rate)
print("Total 1st Try:", total_1st_try)
print("Total 2nd Try:", total_2nd_try)
print("Total 3rd Try:", total_3rd_try)
print("Total 4th Try:", total_4th_try)
print("Total 5th Try:", total_5th_try)
print("Total 6th Try:", total_6th_try)
