speed = float(input('Enter your speed (meter/sec):'))
convert = speed*3.6

if convert > 320:
    print(f'Your speed is {convert} km/h. You are as fast as Peregrine Falcon.')
elif 240 <= convert < 320:
    print(f'Y0ur speed is {convert} km/h. You are as fast as Golden Eagle.')
elif 120 <= convert < 240:
    print(f'Y0ur speed is {convert} km/h. You are as fast as Swift.')
elif 80 <= convert < 120:
    print(f'Your speed is {convert} km/h. You are as fast as Cheetah.')
elif 40 <= convert < 80:
    print(f'Your speed is {convert} km/h. You are as fast as Ostrich.')
elif convert < 40:
    print(f'You are too slow. More exercises needed.')
else: 
    print(f'Your input is incorrect. Please enter another input.')