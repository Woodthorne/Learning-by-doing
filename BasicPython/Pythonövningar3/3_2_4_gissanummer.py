lista = [23, 64, 24, 84, 12, 72, 47, 52, 86, 1]
guess = int(input('Gissa på ett heltal mellan 1 och 100: '))
if guess in lista:
    print('Ha, vilken tur du har, du gissa rätt! Är en på 10 att det sker!')
else:
    print('Aj då, bättre lycka nästa gång.')