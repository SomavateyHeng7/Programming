input_str = input("Enter a string: ")

# Counting vowels
vowels = 'aeiou'
vowel_count = 0
for char in input_str:
    if char.lower() in vowels:
        vowel_count += 1

# Counting spaces
space_count = input_str.count(' ')

# Finding longest word
words = input_str.split()
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Output results
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)
print("Longest word:", longest_word)

