animals = ['katt', 'fågel', 'tvättbjörn', 'ekorre']
userAnimals = input('Mata in några favoritdjur. Använd mellanslag: ').lower().split()
similar = []
n = 0
while n < len(userAnimals):
    if userAnimals[n] in animals:
        similar.append(userAnimals[n])
    n += 1
print(f'Vi har {len(similar)} stycken gemensamma djur.')