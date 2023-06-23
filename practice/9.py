numX = int(input('Enter first number:'))
numY = int(input('Enter second number:'))
numZ = int(input('Enter third number:'))

if numX < numY < numZ:
    print(f'The mid value is {numY}')
elif numY < numX < numZ:
    print(f'The mid value is {numX}')
elif numX < numZ < numY:
    print(f'The mid value is {numZ}')
elif numZ < numX < numY:
    print(f'The mid value is {numX}')
elif numY < numZ < numX:
    print(f'The mid value is {numZ}')
elif numZ < numY < numX:
    print(f'The mid value is {numY}')
else:
    print(f'No mid value')