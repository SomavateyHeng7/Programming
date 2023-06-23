startWeek = int(input('Enter a starting week#:'))
startDate = int(input('Enter a starting date#:'))
duration = int(input('Enter a total number of working days:'))

numofweek = duration//7
deadline_week = numofweek + startWeek
remainder = duration % 7

if remainder == 0:
    deadline_date = 0
else:
    deadline_date = remainder

print(f'===============================================================')
print(f'Starting from month#{ startWeek} and date#{ startDate}')
print(f'The deadline of the project is on week#{deadline_week} and dealine is on date#{deadline_date}')