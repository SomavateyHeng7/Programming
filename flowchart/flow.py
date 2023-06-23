first = 0
second = 0
print('How many input(s)?')
N = int(input())
# N = int(input('How many input(s)?:'))
i = 0 
while i < N:
    num = int(input('Enter positive integers:'))
    if i == 0:
        second = num 
        first = second
    elif num > first:
        second = first
        first = num
    elif num > second:
        second = num
    else:
        print(f'Please enter a positive integer!!!')
    i += 1
print(f'The output number is:')
print(second)
        