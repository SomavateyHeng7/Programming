def easyEncrypt(letter, shift, direction):
    baseLower = ord('a')
    baseUpper = ord('A')
    newString =  []
    for char in letter:
        if char.isalpha():
            if char.islower():
                newChar = ord(char) - baseLower
                if direction == 'l':
                    newChar = (newChar - shift) % 26
                else:
                    newChar = (newChar + shift) % 26
                newString.append(chr(newChar + baseLower))
            else:
                newChar = ord(char) - baseUpper
                if direction == 'l':
                    newChar = (newChar - shift) % 26
                else:
                    newChar = (newChar + shift) % 26
                newString.append(chr(newChar + baseUpper))
        else:
            newString.append(char)
    return(''.join(newString))

def easyDecrypt(letter, shift, direction):
    baseLower = ord('a')
    baseUpper = ord('A')
    newString = []
    for char in letter:
        if char.isalpha():
            if char.islower():
                newChar = ord(char) - baseLower
                if direction == 'l':
                    newChar = (newChar + shift) % 26
                else:
                    newChar = (newChar - shift) % 26
                newString.append(chr(newChar + baseLower))
            else:
                newChar = ord(char) - baseUpper
                if direction == 'l':
                    newChar = (newChar + shift) % 26
                else:
                    newChar = (newChar - shift) % 26
                newString.append(chr(newChar + baseUpper))
        else:
            newString.append(char)
    return(''.join(newString))

letter = input("Enter the message you want to encrpt:")
shift = int(input("The number you want to shift by:"))
direction = str(input("Enter shift direction(left -> l or right -> r):"))

print(f'The original text is  "{letter}"')
encryptedText = easyEncrypt(letter, shift, direction)
print(f'The encrypted text is "{encryptedText}"')
if direction == 'l':
    decryptedText = easyDecrypt(encryptedText,shift, 'r')
    print(f'The decrypted text is "{decryptedText}"')
elif direction == 'r':
    decryptedText = easyDecrypt(encryptedText,shift, 'l')
    print(f'The decrypted text is "{decryptedText}"')
else:
    print(f'The shift the direction much be either (left -> l or right -> r)!!!!')

