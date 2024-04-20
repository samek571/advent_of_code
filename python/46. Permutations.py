from itertools import permutations

class Solution:
    def permute(nums):
        nums = list(permutations(nums))

        # output=[]
        # for i in nums:
        #     output.append(list(i))
        #return output

        for i in range(len(nums)):
            nums[i]=list(nums[i])

        return nums
    print(permute([1,2,4]))
    print(permute([4,3,56,8]))