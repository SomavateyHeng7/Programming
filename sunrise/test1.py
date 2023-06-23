originalList = ['A10', 'BMW320', 'Nissan NSX200', 'Benz 220c']

digitList = []
charList =[]

for item in originalList:
    digit_string = ""
    char_string = ""
    for text in item:
        if text.isdigit():
            digit_string += text
        elif text.isalpha():
            char_string += text
    digitList.append(digit_string)
    charList.append(char_string)

print(f'Lists of digits:', digitList)
print(f'Lists of chars:', charList)