nums = input('Mata in en mängd heltal, separerade av mellanslag: ')
# nums = '1 2 3 4 5 6 7 8 9'
nums = nums.split(' ')
nums.reverse()
odd = []
even = []

while 0 < len(nums):
    if int(nums[0]) % 2 == 0:
        even.append(int(nums.pop(0)))
    else:
        odd.append(int(nums.pop(0)))

step = 0
while step < len(even)-1:
    if even[step] > even[step+1]:
        even.append(even.pop(step))
        if step != 0:
            step -= 1
    else:
        step += 1

step = 0
while step < len(odd)-1:
    if odd[step] > odd[step+1]:
        odd.append(odd.pop(step))
        if step != 0:
            step -= 1
    else:
        step += 1

print('De jämna talen är',end='')
for num in even:
    print('',num,end='')
print()
print('De udda talen är',end='')
for num in odd:
    print('',num,end='')