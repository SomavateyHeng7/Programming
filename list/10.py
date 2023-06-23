original_list = [10,20,30]

# Initialize a variable to store the final integer
single_integer = 0

# Iterate through the list of integers
for i in original_list:
    # Multiply the current integer by 10 raised to the power of its length using `len()` function
    single_integer *= 10**len(str(i))
    # Add the current integer
    single_integer += i

print("Original List:", original_list)
print("Single Integer:", single_integer)
