def mid(x, y, z):
    if x <= y <= z or z <= y <= x:
        return y
    elif y <= x <= z or z <= x <= y:
        return x
    else:
        return z

# Prompt the user to enter three integers
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
z = int(input("Enter the third integer: "))

# Call the mid() function and print the result
middle_value = mid(x, y, z)
print("The middle value is:", middle_value)