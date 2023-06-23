sentence = input('Input String:')
number = 0
for char in sentence:
    if char.isdigit():
        number += 1
if number == 0:
    print(f'There is no digit at all!')
else:
    print(f'There are {number} digits in the string.')