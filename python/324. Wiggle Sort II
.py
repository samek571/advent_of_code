class Solution:
    '''[3,3,3,2,1,1]'''
    '''nlogn is clear, sort it and remember it has even positions and odd positions in certain arragement, by list comprehension we just do a fancy swap. The median is what divided nums in even/odd'''

    "''it got to be something with median getting fount in o(n) which is possible by 3way partition''"
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        mid = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
