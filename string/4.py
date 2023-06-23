sentence = str(input('Enter a sentence:'))
character_count = 0
while True :
    character = str(input('Enter a character:'))
    if character == '-1':
        break
    for char in sentence:
        if char == character:
            character_count += 1
    print(f'Total no. of character {character} in this sentence = {character_count}')
    character_count = 0
