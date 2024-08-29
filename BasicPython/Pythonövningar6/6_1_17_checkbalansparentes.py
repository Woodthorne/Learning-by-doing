def isbracketbalance(string):
    isopen = 0
    for char in string:
        if char == '(':
            isopen += 1
        elif char == ')':
            isopen -= 1
            if isopen < 0:
                return False
    if isopen != 0:
        return False
    else:
        return True
    
if __name__ == '__main__':
    print(isbracketbalance('(())'))
    print(isbracketbalance('(()'))
    print(isbracketbalance(')(())('))
