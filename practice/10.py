age = int(input('Enter your age:'))

if 20 <= age <= 70:
    print(f'You are eligible to buy cannabis.')
elif age <20:
    print(f'You are too young to buy cannabis.')
else:
    print(f'You are too old to buy cannabis.')