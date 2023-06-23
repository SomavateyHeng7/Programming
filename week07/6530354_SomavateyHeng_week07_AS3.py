char = list((input("Input: ").split()))
n = int(input("Enter the value of n: "))
my_list = []

for item in char:
    for i in range(1, n+1):
        my_list.append(item.upper() + str(i))

print("Output:" + " ".join(my_list))