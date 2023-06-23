numberA = [4, 1, 2, 9, 7, 100, 5, 0, 99, 100]
numberB = [100, 10, 200, 25, 7, 20]

# initialize variables to keep track of the lowest difference and the
# two integers that have the lowest difference
lowest_difference = float("inf")
lowest_pair = (0, 0)

# loop through both lists and compare each integer to every other integer
for i in range(len(numberA)):
    for j in range(len(numberB)):
        diff = abs(numberA[i] - numberB[j])         #abs() function is used to return absolute value of a number.
        if diff < lowest_difference:
            lowest_difference = diff
            lowest_pair = (numberA[i], numberB[j])

# print the lowest difference and the two integers that have it
print(f"The Lowest difference between two numbers is : {lowest_difference}")
print(f"Lowest pair: {lowest_pair}")
