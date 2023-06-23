startMonth = int(input('Enter a starting month#:'))
startDate = int(input('Enter a starting date#:'))
duration = int(input('Enter a total number of working days:'))

# Initialize the deadline month and date
deadline_month = startMonth
deadline_date = startDate + duration

totalday = startMonth*30
numofmonth = duration//30
remainder = numofmonth%30  

# Increment the deadline month if necessary
while deadline_date > days_in_month:
    deadline_month += 1
    deadline_date -= days_in_month
    if deadline_month > 12:
        deadline_month = 1
    days_in_month = 31
    if deadline_month in [4, 6, 9, 11]:
        days_in_month = 30
    elif deadline_month == 2:
        days_in_month = 28

print(f'===============================================================')
print(f'Starting from month#{ startMonth} and date#{ startDate}')
print(f'The deadline of the project is on month#{deadline_month} and dealine is {deadline_date}')
