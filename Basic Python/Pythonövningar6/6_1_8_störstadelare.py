def sgd(a,b):
    if a < b:
        a,b = b,a
    if b > 0:
        a = sgd(b,a % b)
    return a

if __name__ == '__main__':
    nums = input('Mata in två heltal: ').split(' ')
    print(f'Talens största gemensamma nämnare är {sgd(int(nums[0]),int(nums[1]))}.')