def copydetect(the_list):
    checked = []
    for element in the_list:
        if element in checked:
            return True
        else:
            checked.append(element)
    return False

if __name__ == '__main__':
    print(copydetect([1,2,3,4,5]))
    print(copydetect([1,2,4,4,5]))