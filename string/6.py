text = input('Enter a sentence:')
for char in text:
    if 65 <= ord(char) <=90 or 97 <= ord(char) <= 122 or ord(char) == 32:
        print(char, end = '')
        