weeks = int(input('Ange antalet veckor: '))
days = int(input('Ange antalet dagar: '))
hours = int(input('Ange antalet timmar: '))

thours = hours + days * 24 + weeks * 168
tdays  = round(days + hours / 24 + weeks * 7, 1)
tweeks = round(weeks + days / 7 + hours / 168, 1)
tyears = round(weeks / 52 + days / 365 + hours / 8760, 2)

print(f'{weeks} veckor, {days} dagar och {hours} timmar är lika med {thours} timmar, {tdays} dagar, {tweeks} veckor eller {tyears} år')
