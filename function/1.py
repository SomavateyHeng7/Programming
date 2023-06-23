def myBio(name,surname,age):   
    if age < 5 or age > 70:
        print(f'Dear {name} {surname}, you should stay home to avoid COVID-19.')
    else:
        print(f'Dear {name} {surname}, Please stay home as much as you can.')

name = input('Enter your name:')
surname = input('Enter your surname:')
age = int(input('Enter your age:'))  

myBio(name,surname,age)