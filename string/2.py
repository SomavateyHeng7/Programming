sentence = str(input('Enter a sentence:'))
character = str(input('Enter a character:'))
character_count = 0
for char in sentence:
    if char == character:
        character_count += 1
print(f'Total no. of character {character} in this sentence = {character_count}')