
original_list = [int(x) for x in input('Enter a multiple integer value:').split()]
result = 0
for i in range(len(original_list)):
    result += original_list[i] * (10 ** i)
    # Add the current integer
    # result += i
print(result)
