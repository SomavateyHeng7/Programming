sList = ['Kalamali' , 'Dragonball', 'George', 'Amomarashiya']

vowel = []

for i in range(len(sList)): 
    vowel = ''
    
    for j in range(len(sList[i])):
        if j == 'A' or j == 'a' or j == 'E' or j == 'e' or j == 'o' or j == 'O' or j == 'u' or j == 'U':
            
            print(f' String with max vowel letters is' , sList)
        else:
            print(f'No string in the list.')
        