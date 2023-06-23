chestsize = int(input('Enter chest size (in cm.):'))
inches = chestsize/2.54

print(f'Your chest size is {inches} inches')
if 32 <= inches< 34:
    print(f'Your chest size is XS.')
elif 34 <= inches< 36:
    print(f'Your chest size is S.')
elif 36 <= inches < 37:
    print(f'Your chest size is M.')
elif 37 <= inches< 40:
    print(f'Your chest size is L.')
elif 40 <= inches< 42:
    print(f'Your chest size is XL.')
else: 
    print(f'Shirt size not found. Try again.')