class Solution:
    def rotate(nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     nums[:] = nums[-1:] + nums[:-1]
        #
        # return nums

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        return nums
    print(rotate([1,2,3,4,5,6,7], 3))

