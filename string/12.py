sentence = input('Input String:')
old = input('Replaced string:')
new = input('Replaced with:')
sentenceList = sentence.split()
outsen = ''
count = 0
for char in sentenceList:
    if char == old:
        if count < 2:
            outsen += new + ' '   
            count += 1
        else: 
            outsen += char + ' '
    else:
        outsen += char + ' '
print(f' The output string: {outsen}')