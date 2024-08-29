def countchar(string,char):
    count = 0
    for i in string:
        if char == i:
            count += 1
    return count

if __name__ == '__main__':
    print(countchar('test','t'))