# pyright: reportUnusedCallResult=false

nums = []

with open("input.txt") as file:
    nums = file.read().split()

l1 = sorted(list(map(lambda x: (x[0], int(x[1])), enumerate(nums[::2]))), key=lambda x : x[1])
l2 = sorted(list(map(lambda x: (x[0], int(x[1])), enumerate(nums[1::2]))), key=lambda x : x[1])

t1 = l1[:100] # testing
t2 = l2[:100] # testing

part1 = (sum(list(map(lambda x:abs(x[0][1]-x[1][1]),list(zip(l1,l2))))))

l_ptr, r_ptr = 0,  0

similarity = 0
count = 0 
while l_ptr < len(l1) and r_ptr < len(l2):
    if l1[l_ptr][1] > l2[r_ptr][1]:
        r_ptr += 1
        continue
    elif l1[l_ptr][1] < l2[r_ptr][1]:
        l_ptr += 1
        continue
        
    elif l1[l_ptr][1] == l2[r_ptr][1]:
        while l1[l_ptr][1] == l2[r_ptr][1]:
            r_ptr += 1
            count += 1

        similarity += l1[l_ptr][1] * count
        r_ptr = 0
        l_ptr += 1
        count = 0
