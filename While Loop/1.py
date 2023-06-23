user = int(input("Enter a positive integer(to terminate enter a negative number):"))
mysum = 0
count = 0
if user < 0:
    print(f'The sum of all positive integer(s) is 0.')
else:
    while user >= 0:
        mysum += user
        count += 1
        user = int(input(f"Enter a positive integer(to terminate enter a negative number):"))
print(f"The total number of positive integers entered is {count}")
print(f"The sum of all positive integer(s) is: {mysum}")