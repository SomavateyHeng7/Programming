sumodd = 0
sumeven = 0
totalodd = 0
totaleven = 0
i = 1

while True:
    num = int(input(f"Number#{i}: "))

    if num == 0:
        break 
    if num % 2 != 0:
        sumodd += num
        totalodd += 1
    else:
        sumeven += num
        totaleven += 1
    i+= 1

print(f"The sum of all odd numbers: {sumodd}")
print(f"The sum of all even numbers: {sumeven}")

if sumodd > sumeven:
    print(f"The winner is", "*" * totalodd)
elif sumodd < sumeven:
    print(f"The winner is", "+" * totaleven)
else:
    print(f"No winner here. Try again.")