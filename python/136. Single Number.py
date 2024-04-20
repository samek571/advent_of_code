class Solution:
    def singleNumber(nums) -> int:
        # #O(n) Hash
        # hash=dict()
        #
        # for i in nums:
        #     if not i in hash: hash[i] = 1
        #     else: hash[i]+=1
        #
        # return min(hash, key=hash.get)

        #O(1) Math
        return 2 * sum(set(nums)) - sum(nums)

    print(singleNumber([1,2,4,2,1]))
    print(singleNumber([1]))
    print(singleNumber([2,2,1]))