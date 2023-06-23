numberA = [4, 1, 2, 9, 7, 100, 5, 0, 99, 100]
numberB = [100, 10, 200, 25, 7, 20]

lowest_difference = float("inf")

for i in range(len(numberA)):
    for j in range(len(numberB)):
        difference = abs(numberA[i] - numberB[j])         #abs() function is used to return absolute value of a number.
        if difference < lowest_difference:
            lowest_difference = difference

print(f"The Lowest difference between two numbers is : {lowest_difference}")
 
