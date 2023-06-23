startQuarter = int(input('Enter a starting quarter#:'))
startDate = int(input('Enter a starting date#:'))
duration = int(input('Enter a total number of working days:'))

if startQuarter == 1 and startDate == 1:
    numofquarter = duration//90
    deadline_quarter = numofquarter
    deadline_date = duration / numofquarter
else:
    startDate = 1
    numofmonth = duration//90
    deadline_month = numofmonth + startQuarter
    remainder = duration % 90
    deadline_date = remainder + startDate
    if duration % 90 == 0:
        deadline_month -= 1
        deadline_date = 90

print(f'===============================================================')
print(f'Starting from quarter#{ startQuarter} and date#{ startDate}')
print(f'The deadline of the project is on quarter#{deadline_quarter} and dealine is on date# {int(deadline_date)}.')
