message = str(input('Enter string:'))
total = 0
lower_count = 0
upper_count = 0
count = 0
numeric_count =0
for char in message:
    if char.isalpha():
        total += 1
        if char.islower():
            lower_count +=1 
        elif char.isupper():
            upper_count += 1 
    elif char.isnumeric():
       numeric_count += 1 
    else:
       count +=1
print(f'Total Alphabet = {total}')
print(f'Uppercase = {upper_count}')
print(f'Lowercase = {lower_count}')
print(f'Numeric = {numeric_count}')
print(f'Other letters (including space) = {count}')
