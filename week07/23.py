num_of_strings = int(input("Enter number of strings: "))
string_list = []

for i in range(num_of_strings):
    string = input("Enter string: ")
    string_list.append(string)

unique_strings = set(string_list)
print("Unique strings:", unique_strings)
