n = int(input("How many numbers?"))
i = 1
smallest = float('inf')
secondsmallest = float('inf')

while i <= n: 
    num = float(input(f"Number#{i}: "))
    if num < smallest:
        smallest = num
    elif num < secondsmallest:
        secondsmallest = num
    i+= 1
print(f'The smallest number is {smallest}')
if n > 1:   
    print(f'The second smallest number is {secondsmallest}')
else:
    print(f'There is no second smallest number.')