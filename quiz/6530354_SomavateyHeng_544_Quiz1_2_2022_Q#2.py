hourNo = int(input('Enter a starting hour#:'))
mins = int(input('Enter a starting minute#:'))
total = int(input('Enter a total number of minutes:'))

hour = total // 60
departH = hour + hourNo
remainder = total % 60

if remainder == 0:
    departMin = 0

else:
    departMin = (remainder + mins) - 1 

print(f'===============================================================')
print(f'Starting from hour#{ hourNo} and min#{ mins}')
print(f'If you have parked {total} mins, the departure time is in hour#{departH} and {departMin} mins.')