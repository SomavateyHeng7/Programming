sentence = input('Input String:')
for char in range(len(sentence)-1, -1 ,-1):
    print(sentence[char], end='')
print()

for char in range(-1, -len(sentence)-1,-1):
    print(sentence[char], end='')
print()

#using while loop
char = len(sentence)-1
while char > -1:
     print(sentence[char], end='')
     char -= 1
print()

char = -1
while char > -len(sentence)-1:
     print(sentence[char], end='')
     char -= 1
print()