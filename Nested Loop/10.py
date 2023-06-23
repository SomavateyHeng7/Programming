print(f'Assume that your date of birth is 1 January')
birthyear = int(input(f'Enter your year of birth (A.D.):'))
presentyear = 2022
for presentyear in range (presentyear,birthyear-1,-1 ):
    print(f'By December {presentyear}, you are {presentyear - birthyear + 1} yearsold')
