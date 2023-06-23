windspeed = float(input('Enter a wind speed in mile/min:'))
convert = windspeed*96.5606

if 0 <= convert< 1:
    print(f'Windspeed is {convert} km/hour and the wind condition is now calm.')
elif 1 <= convert< 25:
    print(f'Windspeed is {convert} km/hour and the wind condition is now light.')
elif 25 <= convert < 40:
    print(f'Windspeed is {convert} km/hour and the wind condition is now moderate.')
elif 40 <= convert< 60:
    print(f'Windspeed is {convert} km/hour and the wind condition is now strong.')
elif convert>= 60:
    print(f'Windspeed is {convert} km/hour and the wind condition is now extreme.')
else: 
    print(f'Wrong input. Wind speed must be a positive value.')