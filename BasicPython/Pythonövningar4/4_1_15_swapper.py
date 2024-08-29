num_list = input('Mata in ett antal heltal separerade av mellanslag: ').split(' ')
for num in num_list:
    if num.lstrip('-').isnumeric:
        num_list[num_list.index(num)] = int(num)
    else:
        print('Bara heltal tillåtna.')
        quit()

step = 1
while step < len(num_list):
    num_list[step-1], num_list[step] = num_list[step], num_list[step-1]
    step += 2
print(num_list)