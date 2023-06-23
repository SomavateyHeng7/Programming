num = int(input("Enter a number: "))
digits = []

# Loop through each digit in the number
while num > 0:
    # Get the last digit of the number
    digit = num % 10
    # Add the digit to the list
    digits.append(digit)
    # Remove the last digit from the number
    num //= 10

# Reverse the order of the list
digits.reverse()

# Print the list of digits
print(digits)
