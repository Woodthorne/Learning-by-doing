num_list = input('Mata in valfri mängd positiva eller negative heltal separerade av mellanslag: ').split(' ')
for num in num_list:
    if num.lstrip('-').isnumeric():
        num_list[num_list.index(num)] = int(num)
    else:
        print('Bara heltal.')
        quit()

num = 0
while num < len(num_list):
    check = 0
    while check < len(num_list):
        if num == check:
            check += 1
            continue
        if num_list[check] == num_list[num]:
            num_list.pop(check)
        else:
            check += 1
    num += 1

print(num_list)