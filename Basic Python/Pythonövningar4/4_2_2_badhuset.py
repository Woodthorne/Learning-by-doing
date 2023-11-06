priser = [0, 50, 100, 70, 70]
kategorier = ['null', 'barn', 'vuxen', 'pensionär', 'student']

while True:
    print('======Välkommen till badhuset======')
    print('HUVUDMENY\n 1. Börja ett nytt köp\n 2. Administrera\n 3. Avsluta')
    val = int(input('Menyval: '))
    if val == 1:
        nya_badare = [0, 0, 0, 0, 0]
        while True:
            print('===============================')
            print('NYTT KÖP\n 1. Lägg till badare\n 2. Ångra badare\n 3. Betala\n 4. Huvudmeny')
            val = int(input('Menyval: '))

            if val == 1:
                print('PRISER\n 1. Barn (50 kr)\n 2. Vuxen (100 kr)\n 3. Pensionär (70 kr)\n 4. Student (70 kr) (Student-ID krävs)')
                val = int(input('Menyval: '))
                if val == 4:
                    studentid = input('Mata in giltigt student-id: ')
                    if len(studentid) != 5 or studentid[0] not in ['A','D','E','T'] or not studentid[1:5].isnumeric or studentid[1] == '0':
                        print('Ogiltigt student-id')
                        continue
                if val in [1,2,3,4]:
                    nya_badare[val] += 1

            elif val == 2:
                print(f'Nuvarande badare:\n 1. Barn ({nya_badare[1]})\n 2. Vuxen ({nya_badare[2]})\n 3. Pensionär ({nya_badare[3]})\n 4. Student ({nya_badare[4]})')
                val = int(input('Vad vill du ta bort? '))
                if val in [1,2,3,4] and nya_badare[val] > 0:
                    nya_badare[val] -= 1

            elif val == 3:
                total_kostnad = []
                for i in range(1,5):
                    total_kostnad.append(nya_badare[i]*priser[i])
                print('Belopp att betala:',sum(total_kostnad),' kronor.')
                betalning = float(input('Mata in motaget belopp i kronor: '))
                if betalning >= sum(total_kostnad):
                    print('Betalning lyckades. Växel tillbaka: ',betalning - sum(total_kostnad))
                    print('Kvitto:')
                    for i in range(1,5):
                        print(f'{nya_badare[i]}x {kategorier[i]}: {total_kostnad[i-1]} kr')
                    print('Totalt',sum(total_kostnad), 'kronor')
                else:
                    print('Otillräcklig betalning.')
                break

            elif val == 4:
                break

    elif val == 2:
        while True:
            print('===============================')
            print(f'ADMINISTRERA\n 1. Ändra priser för barn ({priser[1]})\n 2. Ändra priser för pensionärer ({priser[3]})\n 3. Ändra priser för studenter ({priser[4]})\n 4. Huvudmeny')
            val = int(input('Menyval: '))
            if val == 1:
                priser[1] = input('Ny prissättning för barn: ')
            elif val == 2:
                priser[3] = input('Ny prissättning för pensionärer: ')
            elif val == 3:
                priser[4] = input('Ny prissättning för studenter: ')
            elif val == 4:
                break
    elif val == 3:
        quit()