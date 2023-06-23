def combination(n, r):
    # calculate the factorials of n, r, and n-r
    n_factorial = 1
    for i in range(1, n+1):
        n_factorial *= i
    r_factorial = 1
    for i in range(1, r+1):
        r_factorial *= i
    n_minus_r_factorial = 1
    for i in range(1, n-r+1):
        n_minus_r_factorial *= i
    
    # calculate the combination using the formula
    combination = n_factorial / (r_factorial * n_minus_r_factorial)
    
    # return the result
    return combination

n = int(input('Enter n:'))
r = int(input("Enter r:"))
print(combination(n, r))