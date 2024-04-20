def twoSum (nums, target):
    counteri = 0
    counterj = 0

    for i in nums:
        for j in nums:

            if i+j==target and counterj!=counteri:
                list=[]
                list.append(counteri)
                list.append(counterj)
                return list

            counterj += 1
        counterj=0
        counteri += 1

print(twoSum([2,3,4,5,6,9,0,4], 12))
#print(twoSum([2,11,7,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([7,6,3,2,1,0], 2))