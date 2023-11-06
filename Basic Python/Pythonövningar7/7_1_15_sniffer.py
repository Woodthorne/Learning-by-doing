import os

txt_files = []

def detect_txt():
    # Finds all files in the current directory, and returns all txt-files as a list.
    all_files = os.listdir()
    index = 0
    for file in all_files:
        all_files[index] = file.split('.')
        index += 1
    index = len(all_files)-1
    for reversefile in all_files[::-1]:
        if reversefile[-1] != 'txt':
            all_files.pop(index)
        else:
            all_files[index] = '.'.join(reversefile)
        index -= 1
    return all_files

def sniff(old,new):
    for file in txt_files:
        # Copy the file
        current_lines = []
        with open(file,'r',encoding='utf-8') as f:
            for line in f:
                current_lines.append(line.replace('\n',''))
        
        # Change the contents
        index = 0
        changed = False
        for line in current_lines:
            if old in line:
                current_lines[index] = line.replace(old,new)
                changed = True
            index += 1
        
        # Return to file, if changed
        if changed:
            with open(file,'w',encoding='utf-8') as f:
                for line in current_lines:
                    f.write(f'{line}\n')

if __name__ == '__main__':
    txt_files = detect_txt()
    sniff(input('Ta bort sträng: '),input('Ersätt med: '))
