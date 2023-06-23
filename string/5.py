text = input('Enter a sentence:')
for char in text:
    if char.isalpha() or char.isspace():
        print(char, end = '')
        