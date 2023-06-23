num = int(input('Enter the 3-digits number:'))
d1 = num//100
if d1%2 == 0:
    print(f'I am sure either 2, 4, 6, or 8 must be a left-most digit.')
else:
    print(f'I know that the number you entered starts with either 1, 3, 5, 7, or 9.')