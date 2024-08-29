def cipher(mod):
    line = 0
    while line < len(list_of_lines):
        new_line = ''
        char = 0
        while char < len(list_of_lines[line]):
            new_line += chr(ord(list_of_lines[line][char]) + mod)
            char += 1
        list_of_lines[line] = new_line + '\n'
        line += 1

list_of_lines = []
with open('sample.txt','r') as f:
    for line in f:
        list_of_lines.append(line.strip('\n'))

cipher(1)

with open('sample_coded.txt','w') as f:
    for line in list_of_lines:
        f.write(line)

list_of_lines = []
with open('sample_coded.txt','r') as f:
    for line in f:
        list_of_lines.append(line.strip('\n'))

cipher(-1)

print(list_of_lines)