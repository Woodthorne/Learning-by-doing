def reversesentence(string):
    string = ' '.join(list(reversed(string.split(' '))))
    return string

if __name__ == '__main__':
    print(reversesentence('baklänges. är mening Denna'))