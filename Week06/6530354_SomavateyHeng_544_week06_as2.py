A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = 'MNODSETFGHZABIJPXQWRUCYKLV'
text = input("Enter a message: ")
result = ''
for char in text:
    if char.isupper():
        index = A.find(char)
        result += B[index]
    else:
        result += char
print(result)