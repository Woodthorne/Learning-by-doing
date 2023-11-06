def onlyevenindex(the_list):
    index = 0
    new_list = []
    while index < len(the_list):
        if index % 2 == 0:
            new_list.append(the_list[index])
        index += 1
    return new_list

if __name__ == '__main__':
    print(onlyevenindex([1,2,3,4,5,6,7]))