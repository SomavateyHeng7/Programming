List_1 = [1,3,5,6,7,8]
List_2 = [10,20,30]
List_3 = [11,22,33]

print(List_2 + List_1[1:-1] + List_3)

outList = []
for i in List_2:
    outList.append(i)
for i in range(1,len(List_1)-1):
    outList.append(List_1[i])
for i in List_3:
    outList.append(i)   
print(outList)