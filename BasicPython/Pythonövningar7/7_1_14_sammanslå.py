all_lines = []

def copyFile(filename):
    if len(all_lines) != 0:
        all_lines.append('--------------SEPARATING LINE----------------\n')
    with open(filename,'r') as f:
        for line in f:
            all_lines.append(line)

def mergeFile(filename):
    with open(filename,'w') as f:
        for line in all_lines:
            f.write(line)

if __name__ == '__main__':
    copyFile('file1.txt')
    copyFile('file2.txt')
    copyFile('file3.txt')
    mergeFile('merged.txt')