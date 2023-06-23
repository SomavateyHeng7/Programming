x = [int(x) for x in input('Enter a multiple integer value:').split()]
sum = 0
largest_number = float('-inf')
lowest_number = float('inf')
multiply = 1
for i in x:
    sum += i
    multiply *= i
    if i > largest_number:
        largest_number = i
    if i < lowest_number:
        lowest_number = i
        
print(f'The sum of all the numbers in the list {sum}.')
print(f'The multiplication of all the numbers in the list {multiply}.')
print(f'The largest number is {largest_number}.')
print(f'The lowest number is {lowest_number}.')
