
originalList = ['100hrs', '30mins', 'Jan2023', 'Fx80', 'A100Model']

digits = []
extracted = []

for i in originalList:
    if i.isdigit():
        digits.append(i)
    else:
        extracted.append(i)

print(digits)
print(extracted)