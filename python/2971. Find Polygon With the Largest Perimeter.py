class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pref, res = 0, -1

        for num in nums:
            if num < pref:
                res = num + pref
            pref += num

        return res
