def easyEncrypt(sen, shift):
    baseLower = ord('a')
    baseUpper = ord('A')
    outsen = []
    for c in sen:
        if c.isalpha():
            if c.islower():
                newC = (ord(c)-baseLower+shift)%26
                outsen.append(chr(newC + baseLower))
            else:
                newC = (ord(c)-baseUpper+shift)%26
                outsen.append(chr(newC + baseUpper))
        else:
            outsen.append(c)
    return (''.join(outsen))

def easyDecrypt(sen, shift):
    baseLower = ord('a')
    baseUpper = ord('A')
    outsen = []
    for c in sen:
        if c.isalpha():
            if c.islower():
                newC = (ord(c)-baseLower-shift)%26
                outsen.append(chr(newC + baseLower))
            else:
                newC = (ord(c)-baseUpper-shift)%26
                outsen.append(chr(newC + baseUpper))
        else:
            outsen.append(c)
    return (''.join(outsen))
    
sen = 'I eat 1,000 kcal a day.'
shift = 3
print(f'The original text is  "{sen}"')
encryptedText = easyEncrypt(sen, shift)
print(f'The encrypted text is "{encryptedText}"')
decryptedText = easyDecrypt(encryptedText,shift)
print(f'The decrypted text is "{decryptedText}"')