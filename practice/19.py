# Initialize variables to store the sum of odd integers and even integers
sumodd = 0
sumeven = 0

# Initialize a variable to store the total number of odd integers entered
totalodd = 0

# Initialize a variable to store the total number of even integers entered
totaleven = 0

# Use a while loop to take input until 0 is entered
while True:
  num = int(input("Enter an integer (0 to stop): "))
  
  # If the input is 0, break out of the loop
  if num == 0:
    break
  
  # If the input is odd, add it to the sum of odd integers and increment the total number of odd integers
  if num % 2 != 0:
    sumodd += num
    totalodd += 1
  # Otherwise, add it to the sum of even integers and increment the total number of even integers
  else:
    sumeven += num
    totaleven += 1

# Print the sum of odd integers and even integers
print(f"Sum of odd integers: {sumodd}")
print(f"Sum of even integers: {sumeven}")

# Determine the winner based on the conditions specified
if sumodd > sumeven:
  print(f"The winner is", "*" * totalodd)
elif sumodd < sumeven:
  print(f"The winner is", "+" * totaleven)
else:
  print(f"No winner here. Try again.")