matrixM = [[1,3], [5,7]]
matrixN = [[0.5,1.6, 7.9], [2.2, 4.0, 5.6] , [3.5,9.8,2.9]]

nRow = len(matrixM)
nColumn = len(matrixM[0])
for row in range(nRow):
    for col in range(nColumn):
        print(matrixM[row][col], end=' ')
    print()