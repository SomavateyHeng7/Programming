oriList = ['100hrs', '30mins', 'Jan2023', 'Fx80', 'A100Model']

charList = []
extractList = []

for i in range(len(oriList)):
    digitResult = ''
    extractResult = ''
    for j in range(len(oriList[i])):
        if oriList[i][j].isdigit():
            digitResult += oriList[i][j]
        elif oriList[i][j].isalpha():
            extractResult += "*"
            extractResult += oriList[i][j]

    charList.append(digitResult)
    extractList.append(extractResult)

print("Lists of chars:", charList)
print("Extracted lists:", extractList)