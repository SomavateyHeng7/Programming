def SumofOddPos(nList):
    if len(nList) == 0:
        return 0
    else:
        return nList[0] + SumofOddPos(nList[2:])

def SumofEvenPost(nList):
    if len(nList) < 2:
        return nList[2:]
    else:
        return 
    
nList = [1,20,3,40,5,60]

print(SumofOddPos(nList))
