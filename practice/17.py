height = int(input('Enter your height:'))

if height < 80:
    print(f'Your height is {height} and you are too small for this ride.')
elif 80 < height < 180:
    print(f'You are ok for this ride.')
elif height > 180:
    print(f'Your height is {height} are too tall for this ride.')
else:
    print(f'You can\t enter negative number.')