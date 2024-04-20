class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return (lambda a, b: [a - b, b - a])(set(nums1), set(nums2))
