num_list = input('Mata in ett antal heltal separerade av mellanslag: ').split(' ')
for num in num_list:
    if num.isnumeric:
        num_list[num_list.index(num)] = int(num)
    else:
        print('Bara heltal tillåtna.')
        quit()

step = 0
while step < len(num_list)-1:
    if num_list[step] > num_list[step+1]:
        num_list.append(num_list.pop(step))
        if step != 0:
            step -= 1
    else:
        step += 1

print('Den största differensen mellan två tal är ', num_list[-1] - num_list[0])