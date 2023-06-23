originalList = [ '100hrs', '30mins', 'Jan2023', 'Fx80', 'A100Model']

digits = []
extracted = []

for item in originalList:
    digit_str = ""
    char_str = ""
    for char in item:
        if char.isdigit():
            digit_str += char
        else:
            char_str += "*"
    
    digits.append(digit_str)
    extracted.append(char_str)

print("Lists of digits:", digits)
print("Extracted lists:", [item.rjust(len(item), "*") for item in extracted])
