number = input("Enter a number: ")

# Convert the number to a string and get its length
number_str = str(number)
length = len(number_str)

# Swap the first and last digits
new_number_str = number_str[length-1] + number_str[1:length-1] + number_str[0]

# Convert the new number string back to an integer
new_number = int(new_number_str)

print("The original number was:", number)
print("The new number is:", new_number)
