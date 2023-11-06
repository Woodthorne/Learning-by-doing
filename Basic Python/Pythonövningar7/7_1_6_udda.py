with open('sample.txt','r') as f:
    isudda = True
    for line in f:
        if isudda:
            isudda = False
            print(line.strip())
        else:
            isudda = True