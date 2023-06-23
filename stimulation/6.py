def sum_of_series(n):
    if n == 1:
        return 1
    else:
        return n**5 + sum_of_series(n-1)

n = int(input("Enter the value of n: "))
total = sum_of_series(n)
print("The sum of the series is:", total)
