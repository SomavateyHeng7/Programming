x = [int(x) for x in input('Enter a multiple integer value:').split()]

lowest_number = x[0]
for number in x:
    if number < lowest_number:
        lowest_number = number
print(f'The lowest number is {lowest_number}')