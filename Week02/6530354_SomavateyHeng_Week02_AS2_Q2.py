myNum = int(input('Enter a number:'))
d4 = myNum%10
d3 = (myNum%100)//10
d2 = (myNum%1000)//100
d1 = myNum//1000

summation = d3 + d4

print(f'The result is {summation}')
