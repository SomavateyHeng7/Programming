char = list((input("Input: ").split()))
n = int(input("Enter the value of n: "))
my_list = []

for item in char:
    for i in range(1, n+1):
        if i%2 == 0:
            my_list.append(item.upper() + str(i))
        else:
            my_list.append(item.lower() + str(i))
print("Output:" + " ".join(my_list))