myList = [int(x) for x in input('Enter a multiple integer value:').split()]
# Initialize a variable to store the final integer
single_integer = 0

# Iterate through the list of integers
for i in myList:
    # Multiply the current integer by 10 raised to the power of its length using `len()` function
    single_integer *= 10**len(str(i))
    # Add the current integer
    single_integer += i
print("Single Integer:", single_integer)
