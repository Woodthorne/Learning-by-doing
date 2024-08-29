list_of_lines = []
with open('sample.txt','r') as f1:
    with open('sample_backup.txt','w+') as f2:
        for line in f1:
            if line != f2.readline():
                f2.write(line)