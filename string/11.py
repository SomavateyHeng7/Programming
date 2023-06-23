input_string = "You are my sunshine, you are my everything."
old_substring = "are"
new_substring = "were"

# string = input('Enter a sentence:')
# oldString = input('Enter old string:')
# newString = input('Enter new string to sub:')

output_string = ""
start_index = 0

while start_index < len(input_string):
    index = input_string.find(old_substring, start_index)
    if index == -1:
        output_string += input_string[start_index:]
        break
    output_string += input_string[start_index:index] + new_substring
    start_index = index + len(old_substring)

print(output_string)
