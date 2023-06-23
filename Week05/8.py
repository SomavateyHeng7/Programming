numberA = [1, 52, 36, 25, 8, -12]
numberB = [3, -54, 232, 4, 76, 340]

lowest_difference = float('inf')  # initialize the lowest difference to infinity

for a in numberA:
    for b in numberB:
        difference = abs(a - b)  # calculate the difference between a and b
        if difference < lowest_difference:  # update the lowest difference if necessary
            lowest_difference = difference

print(lowest_difference)  # prints 1
