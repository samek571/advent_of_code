from itertools import chain
class Solution:
    def removeElement(nums, val: int) -> int:
        # output=[]
        # counter=0
        #
        # for i in nums:
        #     if i!= val:output.append(i)
        #     else: counter+=1
        #
        # return list(chain(output, [0]*counter))

        # counter=0
        # for i in nums:
        #     if i == val: counter+=1
        #
        # return len(nums)-counter

        # l= len(nums)
        # if l==0: return 0
        # elif l==1:
        #     if nums[0]==val:
        #         nums[0]=-1
        #         return 1
        #     else: return 0
        #
        # i=0
        # while i<l:
        #     if nums[i]==val:
        #         nums.remove(nums[i])
        #         nums.append(-1)
        #         continue
        #
        #     elif nums[i]==-1: return nums.count(-1)
        #     i+=1
        # return 0

        while nums.count(val)!=0:
            nums.remove(val)

    print(removeElement([0,1,2,2,3,0,4,2], 2))
    print(removeElement([0,1,2,2,3,0,4,2], 1))
    print(removeElement([0,1,2,2,3,0,4,2], 0))
    print(removeElement([3,2,2,3], 3))
    print(removeElement([],7))
    print(removeElement([0],0))