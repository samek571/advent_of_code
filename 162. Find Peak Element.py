class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n <3: return nums.index(max(nums))

        
        # works ebcause by binary search we find ANY local amximum
        low, high = 0, len(nums) - 1
        while low <= high:
            if low == high: return low

            mid = (low + high) // 2
            if nums[mid] < nums[mid + 1]: low = mid + 1
            else: high = mid

        return mid


        # for i in range(1, len(nums)-1):
        #     if nums[i] > max(nums[i+1], nums[i-1]): return i
