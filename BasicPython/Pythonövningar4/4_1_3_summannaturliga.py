num = int(input('Mata in ett positivt heltal: '))
if num > 0:
    sum_of_num = 0
    while num > 0:
        sum_of_num += num
        num -= 1
    print(sum_of_num)