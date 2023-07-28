from itertools import combinations

class Solution:
    def minimumDifference(nums, k) -> int:
        if len(nums) == 1 or k==1:
            return 0

        else:
            nums = sorted(nums, reverse=False)
            minimal = 10 ** 10

            for i in range(len(nums)):
                try:
                    if nums[i+k-1] - nums[i] < minimal and i+k-1 < len(nums) :
                        minimal = nums[i+k-1] - nums[i]
                except IndexError:
                    return minimal

    print(minimumDifference([9,4,1,7], 3))
    print(minimumDifference([12, 40, 18, 90, 44, 22], 3))
    print(minimumDifference([30266,74974,6275,5926], 1))
