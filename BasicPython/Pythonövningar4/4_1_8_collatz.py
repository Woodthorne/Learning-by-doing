num = int(input('Mata in ett positivt heltal: '))
steps = 0
while num > 1:
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    steps += 1
print(steps)