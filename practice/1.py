number = int(input('Enter the number of days:'))
years = number//365
remainder = number%365
month = remainder //30 
week = remainder%30
day = remainder//7

print(f'Total {number} day = {years} year, {month} months, {week} weeks and {day} days.')