class Solution:
    #lenght is always oddbecause 2n+1
    # implementation of bs --> check mid and his neighbor, if non is duplicate its clear the mid is duplicate
    # "recursively" repeat this proccess, knowing whether go up or down is determined easily by 
    # checking if we caught duplicate on the right or on the left from the pair that are next to each other 
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
