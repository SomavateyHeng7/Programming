n = int(input('User input:'))
while n > 0:
    d1 = n % 10 
    n = n // 10
    print(d1)
    
    i = 0
    while i < d1:
        print(d1, end = ' ')
        i +=1
    print()
        