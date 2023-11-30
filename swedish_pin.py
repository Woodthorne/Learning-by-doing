def pin_final(nums: str):
    '''
    Given a string of the first nine digits of a ten digit swedish personal
    number, the function will calculate what the tenth digit would be.

    src: https://sv.wikipedia.org/wiki/Personnummer_i_Sverige#Kontrollsiffran
    '''
    nums = list(nums)
    sum_of_nums = 0
    multiplier = 2
    for n in nums:
        num = int(n) * multiplier
        if num > 9:
            a = num % 10
            b = num // 10
            num = a + b
        sum_of_nums += num
        if multiplier == 1:
            multiplier = 2
        else:
            multiplier = 1
    final_num = 0
    while (sum_of_nums + final_num) % 10 != 0:
        final_num += 1
    
    print(f'{"".join(nums)} adds up to {sum_of_nums} and needs a final {final_num} to complete as {"".join(nums) + str(final_num)}')

if __name__ == '__main__':
    pin_final(input('Input the first 9 digits of a 10 digit swedish pin: '))