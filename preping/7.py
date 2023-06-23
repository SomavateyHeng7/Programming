age = int(input("Enter your age:"))
gender = str(input("Enter your gender:"))

if 0 <= age < 5:
    if gender == 'm' or gender =='M':
        print(f'With you age and gender, a change having obesity is 0%')
    elif gender == 'f' or gender == 'F':
        print(f'With you age and gender, a change having obesity is 0%')
    else:
        print(f'Wrong Input.....Try again.')
elif 5 <= age < 24:
    if gender == 'm' or gender == 'M':
        print(f'With you age and gender, a change having obesity is 11.1%')
    elif gender == 'f' or gender == 'F':
        print(f'With you age and gender, a change having obesity is 9.3%')
    else:
        print(f'Wrong Input.....Try again.')
elif 24 <= age < 44:
    if gender == 'm' or gender =='M':
        print(f'With you age and gender, a change having obesity is 19.9%')
    elif gender == 'f' or gender == 'F':
        print(f'With you age and gender, a change having obesity is 21.3%')
    else:
        print(f'Wrong Input.....Try again.')
elif age > 44:
    if gender == 'm' or gender == 'M':
        print(f'With you age and gender, a change having obesity is 23.2%')
    elif gender == 'f' or gender == 'F':
        print(f'With you age and gender, a change having obesity is 29.2%')
    else:
        print(f'Wrong Input.....Try again.')
else:
    print(f'Wrong Input.....Try again.')