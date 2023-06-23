i = 0
while i < 10:
    j =0
    while j < 5:
        if j % 2 == 0: 
            print('XXX', end = ' ')
        else:
            print('YYY', end = ' ' )
        j += 1
    i += 1
    print()
print('BBB')