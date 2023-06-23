num1= int(input('Enter num1:'))
num2= int(input('Enter num2:'))
num3= int(input('Enter num3:'))

if (num1%num3) == 0 and (num2%num3)==0:
    if num3<10:
        print(f'num3 is a factor of both num1 and num2. Also, num3 is a single-digit integer.')
    else: 
        print(f'num3 is a factor of both num1 and num2. Also, num3 is not a single-digit integer.')
elif (num1%num3) !=0 and (num2%num3)==0:
    if num3<10:
        print(f'num3 is a factor of num2 only. Also, num3 is a single-digit integer.')
    else:
        print(f'num3 is a factor of num2 only. Also, num3 is not single-digit integer.')
elif (num1%num3) ==0 and (num2%num3)!=0:
    if num3<10:
        print(f'num3 is a factor of num1 only. Also, num3 is a single-digit integer.')
    else:
        print(f'num3 is a factor of num1 only. Also, num3 is a not single-digit integer.')
elif (num1%num3) !=0 and (num2%num3)!=0:
    if num3<10:
        print(f'num3 is neither is a factor of num1 nor num2 . Also, num3 is a single-digit integer.')
    else:
        print(f'num3 is neither is a factor of num1 nor num2 . Also, num3 is not a single-digit integer.')
else:
    print(f'Please enter a valid input.')