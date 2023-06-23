mango = 3
durian = 15
budget = int(input('Enter your budget:'))
if budget // durian > 10:
    outDurian = 10
    outMango = (budget-150) // 3
    rem = (budget - 150) % 3
else:
    outDurian = budget // 15
    outMango = budget % 15 // 3
    rem = budget % 15 % 3
print(f'You can buy {outDurian} durian(s) and {outMango} mango(es), and have {rem} USD left.')