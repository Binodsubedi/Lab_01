P_value = float(input('Enter the number of minutes:'))
P_hour = P_value/60
point = ''

if P_hour<=12:
    point = 'am'

if P_hour>12:
    point= 'pm'

if P_hour> 12:

    P_hour -= 12

print(f'the time now is {P_hour} {point}')


