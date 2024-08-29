import math

radius = int(input('Ange en radie: '))
circumference = 2 * math.pi * radius
if circumference > 50:
    print('Stor cirkel')
else:
    print('Liten cirkel')