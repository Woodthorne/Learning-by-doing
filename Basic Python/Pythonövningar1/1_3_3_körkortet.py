driver = input('Har du körkort?(j/n): ').lower()
age = int(input('Ange din ålder: '))
if age >= 18:
    if driver == 'j' or driver == 'ja':
        print('Gratulerar! du får köra på vägarna!')
    if driver == 'n' or driver == 'nej':
        print('Du får ta körkort!')
else:
    if driver == 'j' or driver == 'ja':
        print('Omöjligt! Man måste vara 18 år eller äldre för att ta körkort!')
    if driver == 'n' or driver == 'nej':
        print('Du får vänta tills du är 18 för att ta körkort.')
