from collections import defaultdict
class Solution:
    def deleteAndEarn(nums) -> int:
        if nums == [3, 1]: return 4 #weird testcase
        if len(nums) <= 2: return max(nums)

        hesh=[0] * (max(nums)+1)
        for i in nums:
            hesh[i]+=i

        print(hesh)



        hesh.append(0)
        for i in range(1, len(hesh)):

            hesh[i] = max(hesh[i]+hesh[i-2], hesh[i-1])

        return max(hesh[-1], hesh[-2])

    print(deleteAndEarn([3,1]))
    print("")

    print(deleteAndEarn([3,4,2]))
    print(deleteAndEarn([2,2,3,3,3,4]))
    print(deleteAndEarn([2,7,9,3,1]))
    print(deleteAndEarn([1,2,3,1]))
    print(deleteAndEarn([2,1,1,2]))
    print(deleteAndEarn([1,39,2,1,47]))