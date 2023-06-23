originalList = ['100hrs', '30mins', 'Jan2023', 'Fx80', 'A100Model']

digits = []
strings = []

for item in originalList:
    temp = ''
    for char in item:
        if char.isdigit():
            temp += char
        else:
            temp += '*'
    if temp.isdigit():
        digits.append(temp)
    else:
        strings.append(temp)

print("Lists of digits:", digits)
print("Extracted lists:", strings)