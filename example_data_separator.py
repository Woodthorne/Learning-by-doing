# This program extracts particular data from a file.
# Made as part of a repetition lecture.

import os

def extract_data(filename) -> list:
    if os.path.exists(filename):
        output = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                current_list = line.split(':')
                new_list = [current_list[0].split('-')[1]]
                new_list.append(current_list[1])
                new_list.append(current_list[2].split('_')[1].split(';')[0])
                new_list.append(current_list[2].split('>')[1])
                output.append(new_list)
        return output
    else:
        print('File does not exist. Closing program.')
    return output

if __name__ == '__main__':
    extracted_data = extract_data(input('Input exact file name: '))
    for line in extracted_data:
        print(line)