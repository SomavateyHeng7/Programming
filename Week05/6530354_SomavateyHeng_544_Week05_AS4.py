numberA = [1, 52, 36, 25, 8, -12] 
numberB = [3, -54, 232, 4, 76, 340]
                                             
lowest_difference = float("inf")
#Compare list A index 0 and index 1
for i in range(len(numberA)):
    for j in range(i+1,len(numberA)):
        difference = abs(numberA[i] - numberA[j])         #abs() function is used to return absolute value of a number.
        if difference < lowest_difference:
            lowest_difference = difference
#Compare list B index 0 and index 1
for A in range(len(numberB)):
    for B in range(  A + 1, len(numberB)):
        difference = abs(numberB[A] - numberB[B])         #abs() function is used to return absolute value of a number.
        if difference < lowest_difference:
            lowest_difference = difference
#compare List A index 0 to list B index 0
for C in range(len(numberA)):
    for D in range(0, len(numberB)):
        difference = abs(numberA[C] - numberB[D])         #abs() function is used to return absolute value of a number.
        if difference < lowest_difference:
            lowest_difference = difference

print(f"The Lowest difference between two numbers is : {lowest_difference}")