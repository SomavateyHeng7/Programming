num = int(input("Input number:"))
reverse = 0 
sumofevendigit = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    if digit % 2 == 0:
        sumofevendigit += digit
    num //= 10

print(f'Output number1: {reverse}')
print(f'Output number2: {reverse} + {sumofevendigit} = {reverse + sumofevendigit}')   
    
