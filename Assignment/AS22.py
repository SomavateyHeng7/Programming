myNum = int(input('Enter a number:'))
hundreds = myNum % 100
remainder = (myNum % 10) // 10

summation = hundreds + remainder

print(f'The result is {summation}')