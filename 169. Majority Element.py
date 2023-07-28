class Solution:
    def majorityElement(nums) -> int:

        #O(n) and O(n)
        hesmabp=dict()

        for i in nums:
            if i not in hesmabp: hesmabp[i]=1
            else: hesmabp[i]+=1

        return max(hesmabp, key= lambda x: hesmabp[x])


    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
    print(majorityElement([5]))
    print(majorityElement([3,1,1,3,3,11,1,1]))
    print(majorityElement([3,3,3,3,3,99]))