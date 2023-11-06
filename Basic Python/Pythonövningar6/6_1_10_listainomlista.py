def holdslist(the_list):
    for item in the_list:
        if type(item) == list:
            return True
    return False

if __name__ == '__main__':
    print(holdslist([1,2,3,[],5]))
    print(holdslist([1,2,3,4,5]))