class Solution:
    def findDuplicate(nums) -> int:
        #Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]: return nums[j]

        hovno=sorted(nums)
        for i in range(1, len(hovno)):
            if hovno[i] == hovno[i-1]: return hovno[i]

    print(findDuplicate([3,1,4,4,2]))
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([1,1]))