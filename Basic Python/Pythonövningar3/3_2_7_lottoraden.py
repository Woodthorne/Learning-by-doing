winningNums = ['1', '2', '3', '4', '5', '6', '7']
playerNums = []
count = 0
correct = 0
while len(playerNums) < len(winningNums):
    num = input(f'Skriv in tal {count+1} mellan 1 och 35: ')
    if num not in playerNums:
        if num in winningNums:
            print('Grattis, du är ett steg närmare vinsten!')
            correct += 1
        playerNums.append(num)
        count += 1
    else:
        print('Skriv olika tal. Inte fuska!')
if correct == len(winningNums):
    print('Gratulerar!! Du har vunnit äran att ha alla rätt! Grattis!')