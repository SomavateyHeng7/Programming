startMonth = int(input('Enter a starting month#:'))
startDate = int(input('Enter a starting date#:'))
duration = int(input('Enter a total number of working days:'))

if startMonth == 1 and startDate == 1:
    numofmonth = duration//30
    deadline_month = numofmonth
    deadline_date = duration / numofmonth
else:
    startDate = 1
    numofmonth = duration//30
    deadline_month = numofmonth + startMonth
    remainder = duration % 30
    deadline_date = remainder + startDate
    if duration % 30 == 0: # could be remainder == 0
        deadline_month -= 1
        deadline_date = 30

print(f'===============================================================')
print(f'Starting from month#{ startMonth} and date#{ startDate}')
print(f'The deadline of the project is on month#{deadline_month} and dealine is {int(deadline_date)}.')
