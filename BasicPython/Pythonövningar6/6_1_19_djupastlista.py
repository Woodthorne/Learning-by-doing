def detectdepth(the_list):
    if type(the_list) != list:
        return 0
    list_of_deep = []
    for i in the_list:
        list_of_deep.append(detectdepth(i))
    if len(list_of_deep) == 0:
        return(1)
    return max(list_of_deep)+1

if __name__ == '__main__':
    print(detectdepth([[],[[[]]],[],]))