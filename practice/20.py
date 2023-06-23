numA = int(input("Enter the first integer: "))
numB = int(input("Enter the second integer: "))

# Ensure that numA is the lower integer and numB is the higher integer
if numA > numB:
    numA, numB = numB, numA

# Keep track of the sum of the printed numbers
sum = 0

# Print the numbers from numA to numB (inclusive)
# Stop if the sum is greater than 4 times the highest value
i = numA
while i <= numB and sum <= 4 * numB:
    # Only print the number if it is not divisible by 5
    if i % 5 != 0:
        print(i)
        sum += i
    i += 1