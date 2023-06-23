def matrixMultiplication(mat1, mat2):
    """
    Perform matrix multiplication on two matrices and return the result.
    """
    # Check if the matrices can be multiplied
    if len(mat1[0]) != len(mat2):
        raise ValueError("Matrix dimensions are not compatible for multiplication")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result

# Prompt the user to input the size and values of two matrices
n1 = int(input("Enter the number of rows of matrix 1: "))
m1 = int(input("Enter the number of columns of matrix 1: "))
mat1 = []
for i in range(n1):
    row = [int(x) for x in input(f"Enter the values of row {i+1} of matrix 1: ").split()]
    mat1.append(row)

n2 = int(input("Enter the number of rows of matrix 2: "))
m2 = int(input("Enter the number of columns of matrix 2: "))
mat2 = []
for i in range(n2):
    row = [int(x) for x in input(f"Enter the values of row {i+1} of matrix 2: ").split()]
    mat2.append(row)

# Multiply the matrices and print the result
result = matrixMultiplication(mat1, mat2)
print("The result of matrix multiplication is:")
for row in result:
    print(row)
