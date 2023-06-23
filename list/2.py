x = [int(x) for x in input('Enter a multiple integer value:').split()]
multiply = 1
for i in x:
    multiply *= i
print(multiply)