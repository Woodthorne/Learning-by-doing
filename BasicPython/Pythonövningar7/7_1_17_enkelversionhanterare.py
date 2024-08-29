from datetime import datetime

def backup(filename):
    with open(filename,'r',encoding='utf-8') as f:
        backup_lines = f.readlines()
    backupname = filename.replace('.txt',datetime.now().strftime('-%H-%M-%S')) + '.txt'
    with open(backupname,'w',encoding='utf-8') as f:
        for line in backup_lines:
            f.write(line)

if __name__ == '__main__':
    backup('sample.txt')