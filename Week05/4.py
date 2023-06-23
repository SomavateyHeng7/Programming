numbers = [4, 1, 2, 9, 7, 100, 5, 0, 99, 100]

# initialize variables to keep track of the lowest difference and the
# two integers that have the lowest difference
lowest_difference = float("inf")
lowest_pair = (0, 0)

# loop through the list and compare each integer to every other integer
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        diff = abs(numbers[i] - numbers[j])
        if diff < lowest_difference:
            lowest_difference = diff
            lowest_pair = (numbers[i], numbers[j])

# print the lowest difference and the two integers that have it
print(f"Lowest difference: {lowest_difference}")
print(f"Lowest pair: {lowest_pair}")
