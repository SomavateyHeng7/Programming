MyList = list((input("Enter words: ").split()))
count = 0
for char in MyList:
    if len(char) >= 4 and (char[0:2] == char[-1:-3:-1]):
        count += 1
print(f'The number of words that meet the requirements is: {count}')