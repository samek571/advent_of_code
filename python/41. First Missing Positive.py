class Solution:
    def firstMissingPositive(nums) -> int:

        n=len(nums)
        not_contains_one = True
        i=n-1

        #O(n) -> removing negatives and numbers higher than len(nums)
        while i!= -1:
            if nums[i] == 1: not_contains_one=False
            elif nums[i]<1 or nums[i]>n: nums[i]=1
            i-=1

        #O(1) -> basic requirement checker
        if not_contains_one:
            return 1

        #O(n) -> marking
        for element in range(n):
            index = abs(nums[element])-1
            if nums[index] > 0: nums[index] *= -1


        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

    print(firstMissingPositive([2,1]))
    print(firstMissingPositive([3, 4, -1, 1, 2, 0]))
    print(firstMissingPositive([1,1,5,7,7,3,2,2]))
    print(firstMissingPositive([4, 7, 3, 4, 8,1, 9]))
