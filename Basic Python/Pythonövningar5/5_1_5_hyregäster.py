residents = {}
letters = ['A', 'B']

for building in range(1,7):
    residents[building] = {}
    for entrance in letters:
        residents[building][entrance] = {}
        for unit in range(1,11):
            residents[building][entrance][unit] = []

residents[1]['A'][1].append(['Joakim von Anka','155','Kapitalist','1-800-RICH'])

while True:
    print('==========MENY==========')
    print('För inspektion, mata in önskad lägenhet.\nDu kan även flytta in en ny person genom\natt skriva "flytta" eller avsluta genom\natt skriva "avsluta".')
    opt = input('Menyval: ').upper()
    if opt == 'FLYTTA':
        moving_to = input('Vilken lägenhet flyttas till: ').upper()
        mover_info = input('Ange personens namn, ålder, yrke och telefonnummer separerade av kommatecken(,): ')
        residents[int(moving_to[0])][moving_to[1]][int(moving_to[2])].append(mover_info.split(','))
    elif opt == 'AVSLUTA':
        quit()
    else:
        if len(residents[int(opt[0])][opt[1]][int(opt[2])]) > 0:
            print(' ======================')
            print(f'Boende på address {opt}:',end='')
            for occupant in residents[int(opt[0])][opt[1]][int(opt[2])]:
                print('\nNamn: ',occupant[0])
                print('Ålder:',occupant[1],'år')
                print('Yrke: ',occupant[2])
                print('Tel #:',occupant[3])
        else:
            print('Denna lägenhet är tom.')