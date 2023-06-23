message = str(input('Enter string:'))
lower_count = 0
upper_count = 0
space_count = 0
for char in message:
   if char.islower():
       lower_count +=1 
   elif char.isupper():
       upper_count += 1
   else:
       space_count +=1
print(f'{upper_count} Uppercase ')
print(f'{lower_count} Lowercase ')
print(f'{space_count} Spaces ')
message.swapcase()
print(f'{message.swapcase()} ')

