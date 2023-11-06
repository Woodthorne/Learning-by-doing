def findsmallestlarger(numlist,num):
    if max(numlist) > num:
        smallest_larger = max(numlist)
        for i in numlist:
            if smallest_larger > i > num:
                smallest_larger = i
        return smallest_larger
    else:
        print('Alla tal i listan är mindre.')

if __name__ == '__main__':
    print(findsmallestlarger([1,2,3,4,5,6,7,8],4))