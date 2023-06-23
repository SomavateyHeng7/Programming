value = float(input("How many numbers?"))
i = 1
total = 0
mypositivesum = 0
mynegativesum = 0
while i <= value:
    value = float(input(f'Number#{i}:'))
    total += value
    i+=1
    if value < 0:
        mynegativesum += value
    else :  
        mypositivesum += value
    
    #i+=1
        
print(f'The average of these number is {total/value}')
print(f'The average of these number is {mypositivesum}')
print(f'The average of these number is {mynegativesum}') 