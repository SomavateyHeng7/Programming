n = int(input('Enter n:'))
i = 1
total = 0 
while i <= n:
    if i != n:
        print(i, end = '+')
    else: 
        print(i, end = '=')
    total += i
    i += 1
print(total)