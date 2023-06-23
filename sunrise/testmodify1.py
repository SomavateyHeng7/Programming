oriList = ['100hrs', '30mins', 'Jan2023', 'Fx80', 'A100Model']

digitList = []
extractList = []

for i in range(len(oriList)):
    digitResult = ''
    extractResult = ''
    for j in range(len(oriList[i])):
        if oriList[i][j].isdigit():
            digitResult += oriList[i][j]
            extractResult += "*"
        else:
            extractResult += oriList[i][j]

    digitList.append(digitResult)
    extractList.append(extractResult)

print("Lists of digits:", digitList)
print("Extracted lists:", extractList)