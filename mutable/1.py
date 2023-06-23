def isOdd(n):
    if n % 2 == 1:    # checks if the remainder of n divided by 2 is 1
        return True   # if the remainder is 1, n is odd
    else:
        return False  # if the remainder is 0, n is even

# ask the user for an input
n = int(input("Enter a number: "))
print(isOdd(n))
# call the isOdd function with the user's input
if isOdd(n):
    print(n, "is odd")
else:
    print(n, "is even")
