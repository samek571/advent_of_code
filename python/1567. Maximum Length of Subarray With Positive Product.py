class Solution:
    def getMaxLen(nums) -> int:

        left = 0
        count = 0
        res = 0
        rightMostNegative = None
        leftMostNegative = None
        for right in range(len(nums) + 1):
            if right == len(nums) or nums[right] == 0:
                if count % 2 == 1:
                    res = max([res, right - leftMostNegative - 1, rightMostNegative - left])
                else:
                    res = max(res, right - left)
                left = right + 1
                count = 0
            else:
                if nums[right] < 0:
                    count += 1
                    if count == 1:
                        leftMostNegative = right
                        rightMostNegative = right
                    else:
                        rightMostNegative = right

        return res

    print(getMaxLen([1,-2,-3,4]))
    print(getMaxLen([0,1,-2,-3,-4]))
    print(getMaxLen([-1,-2,-3,0,1]))