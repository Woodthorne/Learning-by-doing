list_of_lines = []
with open('sample.txt','r') as f:
    for line in f:
        list_of_lines.append(line)

print(list_of_lines)

with open('sample_copy.txt','w') as f:
    for line in list_of_lines:
        f.write(line)