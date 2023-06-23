week = int(input('Enter weeks:'))
day = int(input('Enter days:'))
Hweek = week * 168
Hday = day * 24
hour = Hweek + Hday

print(f'The total number of hours is {hour} hours.')