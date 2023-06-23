MyList = list((input("Input ").split()))
unique = []
for i in range(len(MyList)):
    if MyList[i] not in unique:
        unique.append(MyList[i])
print("Output:" + ' '.join(unique))
