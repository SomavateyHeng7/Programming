def mid(x, y, z):
    list = [x, y, z]
    list.sort()
    return list[1]

x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
z = int(input("Enter the third integer: "))

middle = mid(x, y, z)

print("The middle value is:", middle)
