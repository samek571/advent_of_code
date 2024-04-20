class Solution:
    def triangleNumber(nums) -> int:
        if len(nums)<3: return 0

        nums.sort()
        valid=0

        for k in range(len(nums)-1, -1, -1):
            i, j = 0, k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    valid += j-i
                    j -= 1
                else: i += 1

        return valid


    print(triangleNumber([1,2,3,4,5,6]))
    print(triangleNumber([2,2,3,4]))
    print(triangleNumber([4,2,3,4]))
