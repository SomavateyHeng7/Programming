matrix = [[1, 0, 1, 0], [1, 1, 0, 1], [2, 0, 1, 0], [0, 1, 0, 1]]

# Loop through each row of the matrix
for row in matrix:
    # Loop through each element of the row
    for element in row:
        # Print the element followed by a space
        print(element, end=" ")
    # Print a newline character to move to the next row
    print()
