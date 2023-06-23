heroName = "Superman"
length_n = len(heroName)
name = str(input("Enter your name:"))
lengthofstring = len(name)

if lengthofstring > length_n:
    print(f'You are stronger than Superman.')
elif lengthofstring < length_n:
    print(f'You are weaker than an ant.')
else:
    print(f'It cannot be number.')