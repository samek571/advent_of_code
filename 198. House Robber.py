class Solution:
    def rob(nums) -> int:
        if len(nums) <= 2: return max(nums)

        nums.append(0)
        for i in range(1, len(nums)):

            nums[i] = max(nums[i]+nums[i-2], nums[i-1])

        print(nums)
        return max(nums[-1], nums[-2])


    print(rob([2,7,9,3,1]))
    print(rob([1,2,3,1]))
    print(rob([2,1,1,2]))
    print(rob([1,39,2,1,47]))