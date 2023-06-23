num = int(input('Enter the 3-digit number:'))

d3 = num%10
d2 = (num%100)//10
d1 = num//100

if (d1 + d2 + d3)%2 ==0:
    print(f'Sum of all the digits is an even number.')
else:
    print(f'Sum of all digits is not an even number.')