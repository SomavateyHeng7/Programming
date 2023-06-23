x = 1 
def doSth(): 
    global x 
    x = 20+5 
    print('Value of x inside a function: ', x) 
    
print('Value of x outside a function: ', x) 
doSth() 
print('Value of x outside a function: ', x)