def matrixMultiplication(mat1,mat2):
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])

    if col1 != row2:
        return "Error alert!!! Cannot multiply matrices with these dimensions."

    result = [[0 for j in range(col2)] for i in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

row1 = int(input("Enter the number of rows for matrix 1: "))
col1 = int(input("Enter the number of columns for matrix 1: "))
row2 = int(input("Enter the number of rows for matrix 2: "))
col2 = int(input("Enter the number of columns for matrix 2: "))

mat1 = []
mat2 = []

print("Enter the values of matrix 1:")
for i in range(row1):
    row = []
    for j in range(col1):
        number = int(input("Enter the value at row " + str(i+1) + " column " + str(j+1) + ": "))
        row.append(number)
    mat1.append(row)    #add the row to the list

print("Enter the values of matrix 2:")
for i in range(row2):
    row = []
    for j in range(col2):
        number = int(input("Enter the value at row " + str(i+1) + " column " + str(j+1) + ": "))
        row.append(number)
    mat2.append(row)

result = matrixMultiplication(mat1, mat2)

if type(result) == str:
    print(result)
else:
    print("Result:")
    for row in result:
        print(row)