from collections import Counter
class Solution:
    def singleNumber(nums):
        # #za ktore sa treba hanbit jak pes
        # if len(nums)==2:
        #     return nums
        #
        # sum_of_those_two = 2 * sum(set(nums)) - sum(nums)
        # #print(sum_of_those_two)
        #
        # for one in range(len(nums)):
        #     if (sum_of_those_two-nums[one] in nums):
        #         if (sum_of_those_two // 2 != nums[one]): return [nums[one], sum_of_those_two-nums[one]]

        #still not O(1) on space
        c=Counter(nums)
        res=[]
        for i in c:
            if c[i]==1:
                res.append(i)
        return res


    print(singleNumber([1,2,1,3,2,5]))
    print(singleNumber([-1,0]))
    print(singleNumber([0,1]))

    print(singleNumber([0,5, 5, 7]))
    print(singleNumber([6,6, 1,2, 99,99]))
    print(singleNumber([6, 6, 1, 2,2, 99, 99, 11]))