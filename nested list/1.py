List_1 = [int(x) for x in input('Enter a multiple integer value:').split()]
List_2 = [int(x) for x in input('Enter a multiple integer value:').split()]

if all(x in List_2 for x in List_1):
    print("Yes")
else:
    print("No")