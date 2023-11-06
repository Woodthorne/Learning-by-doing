def splitter(string,split):
    list_of_string = []
    step = 0
    while step < len(string):
        if string[step] == split:
            list_of_string.append(string[0:step])
            string = string[step+1::]
            step = -1
        step += 1
    return list_of_string

if __name__ == '__main__':
    print(splitter('Testar att skriva en mening.',' '))