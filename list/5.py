sample_list = list((input('Enter a multiple value:').split()))
count = 0
for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
print(count)

