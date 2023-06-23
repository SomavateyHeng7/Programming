oriList = ['A10', 'BMW320', 'Nissan NSX200', 'Benz 220c'] #original list

digitList = []
charList = []

for i in range(len(oriList)):
    digitResult = ''
    charResult = ''
    for j in range(len(oriList[i])):
        if oriList[i][j].isdigit():
            digitResult += oriList[i][j]
        elif oriList[i][j].isalpha():
            charResult += oriList[i][j]
            
    digitList.append(digitResult)
    charList.append(charResult)

print("Lists of digits:", digitList)
print("Lists of characters:", charList)