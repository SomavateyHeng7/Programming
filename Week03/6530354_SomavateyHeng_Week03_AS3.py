myNum = int(input('Enter 5-digits number:'))

d5 = myNum%10
d4 = (myNum%100)//10
d3 = (myNum%1000)//100
d2 = (myNum%10000)//1000
d1 = myNum//10000

if 0 < myNum < 10000:
    print(f'Wrong Input. Try Again.')
elif (d1+d5) > (d2+d3+d4):
    print(f'The output is {(d2*100)+(d3*10)+d4}')
elif(d1+d5)==(d2+d3+d4):
    print(f'The output is {(d1*1000)+(d2*100)+(d4*10)+d5}')
elif (d1+d5) < (d2+d3+d4):
    print(f'The output is {(d1*10)+d5}')
else:
    print(f'The number enter cannot be negative!!!')