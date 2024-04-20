class Solution:
    def removeDuplicates(nums) -> int:
        i=1
        while i<len(nums):
            if nums[i-1] == nums[i]:
                nums.remove(nums[i])
                continue
            i+=1

        return nums
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4,4]))
    print(removeDuplicates([1,1,2,2]))
    print(removeDuplicates([]))