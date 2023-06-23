NumList = [1, 4.9, 4, 'Five', 6, 7, 'Eight', 100.2, 15]

IntList = []
FloatList = []
StrList = []

i=0
while i <len(NumList):
    if isinstance(NumList[i], int):
        IntList.append(NumList[i])
    elif isinstance(NumList[i], float):
        FloatList.append(NumList[i])
    elif isinstance(NumList[i], str):
        StrList.append(NumList[i])
    i+=1
print("IntList:", IntList)
print("FloatList:", FloatList)
print("StrList:", StrList)