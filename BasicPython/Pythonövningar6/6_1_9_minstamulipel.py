def lcm(a,b):
    c = abs(a*b)/sgd(a,b)
    return c

def sgd(a,b):
    if a < b:
        a,b = b,a
    if b > 0:
        a = sgd(b,a % b)
    return a

if __name__ == '__main__':
    nums = input('Mata in två heltal: ').split(' ')
    print(f'Talens minsta gemensamma multipel är {lcm(int(nums[0]),int(nums[1]))}.')