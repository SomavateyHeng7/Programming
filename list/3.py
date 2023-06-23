x = [int(x) for x in input('Enter a multiple integer value:').split()]

largest_number = x[0]
for number in x:
    if number > largest_number:
        largest_number = number
print(f'The largest number is {largest_number}')