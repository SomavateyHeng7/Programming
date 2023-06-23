NumList = [1, 4.9, 4, 'Five', 6, 7, 'Eight', 100.2, 15]

IntList = []
FloatList = []
StrList = []

for item in NumList:
    if isinstance(item, int):
        IntList.append(item)
    elif isinstance(item, float):
        FloatList.append(item)
    elif isinstance(item, str):
        StrList.append(item)

print("IntList:", IntList)
print("FloatList:", FloatList)
print("StrList:", StrList)
