class Solution:
    def rob(nums) -> int:
        if len(nums) <= 3: return max(nums)

        nums1= [0,0] + nums[1:]
        nums = [0,0] + nums[:-1]
        for i in range(2, len(nums)):

            nums[i] = max(nums[i]+nums[i-2], nums[i-1])
            nums1[i] = max(nums1[i]+nums1[i-2], nums1[i-1])

        print(nums)
        return max(nums[-1], nums1[-1])

    print(rob([2,7,9,3,1]))
    print(rob([2,1,1,2]))
    print(rob([1,39,2,1,47]))
    print(rob([2,3,2]))
    print(rob([1,2,3,1]))
    print(rob([1,2,3]))