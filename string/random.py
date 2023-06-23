string = input('Enter a sentence:')
oldString = input('Enter the string you want to sub:')
newString = input('Enter new string to sub:')

output_string = ""
start_index = 0

while start_index < len(string):
    index = string.find(oldString, start_index)
    if index == -1:
        output_string += string[start_index:]
        break
    output_string += string[start_index:index] + newString
    start_index = index + len(oldString)

print(output_string)
