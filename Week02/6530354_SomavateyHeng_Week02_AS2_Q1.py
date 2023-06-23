week = int(input('Enter week:'))
hour = int(input('Enter hours:'))
days = week * 7
day = hour//24
Totalday= days + day

print(f'The total number of days is {Totalday}')