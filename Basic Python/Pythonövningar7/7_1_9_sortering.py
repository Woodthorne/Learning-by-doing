list_of_lines = []
with open('sample.txt','r') as f:
    key = 0
    for line in f:
        list_of_lines.append(line)

list_of_lines.sort()
print(list_of_lines)

with open('sample.txt','w') as f:
    for line in list_of_lines:
        f.write(line)