def countvowel(string):
    vowels = ['a','o','u','å','e','i','y','ä','ö']
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    print(countvowel('testar att skriva massa ord'))