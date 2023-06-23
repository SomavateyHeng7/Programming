stationA = int(input('Enter A\'s starting station#:'))
stationB = int(input('Enter B\'s starting station#:'))
nRound = 1
while stationA != stationB:
    stationA = (stationA + 1) % 20