n = int(input('Enter n:'))
i = 1
total = 1
print(f'{n}! = ', end = '')
if n ==0 or n==1:
    print(f'{n}! = 1')
else:
    while i <= n:
        if i != n:
            print(i, end = 'x')
        else: 
            print(i, end = '=')
        total *= i
        i += 1
print(total)