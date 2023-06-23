numbers = [4, 1, 2, 9, 7, 100, 5, 0, 99, 100]

lowest_difference = float("inf")

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        difference = abs(numbers[i] - numbers[j])        #abs() function is used to return absolute value of a number.
        if difference < lowest_difference:
            lowest_difference = difference

print(f"The lowest difference between two numbers is : {lowest_difference}")