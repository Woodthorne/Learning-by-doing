num = int(input('Mata in ett positivt heltal: '))
num_fact = 1
while num > 0:
    num_fact *= num
    num -= 1
print(num_fact)