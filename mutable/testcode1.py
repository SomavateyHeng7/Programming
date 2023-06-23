def mutableList(aList): 
    aList.append(10) 
    print('Value of List aList inside a function: ', aList) 
a = [1,2,3] 
print('Value of List a outside a function: ', a) 
mutableList(a) 
print('Value of List a outside a function: ', a)