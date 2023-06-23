startingWeek = int(input('Enter a starting week#: '))
startingDate = int(input('Enter a starting date#: '))
duration = int(input('Enter a total number of working days: '))
numofWeek = duration // 7
numofDays = duration % 7

if startingDate + numofDays - 1 <= 7:
    endingWeek = startingWeek + numofWeek
    endingDate = startingDate + numofDays - 1
else:
    endingWeek = startingWeek + numofWeek + 1
    endingDate = startingDate + numofDays - 1 - 7

print(f'Starting from week# {startingWeek} and date# {startingDate},')
print(f'the deadline of the project is in Week#{endingWeek} on date# {endingDate}')