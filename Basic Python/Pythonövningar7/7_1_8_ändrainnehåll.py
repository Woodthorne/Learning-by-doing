replace = input('Vad ska bort? ')
use = input('Vad ska användas istället? ')
file_text = []
with open('sample.txt','r') as f:
    for line in f:
        file_text.append(line)

step = 0
while step < len(file_text):
    if replace in file_text[step]:
        file_text[step] = use.join(file_text[step].split(replace))
    step += 1

with open('sample.txt','w') as f:
    for line in file_text:
        f.write(line)