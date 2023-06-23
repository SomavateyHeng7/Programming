sentence = str(input('Write a sentence:'))
for char in sentence:
    if char.islower():
        letter = char(ord(sentence)-32)
        print(letter)
    else:
        print()