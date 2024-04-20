class Solution:
    def maxSubArray(nums) -> int:
        output=nums[0]

        current=0
        for value in nums:
            if current<0: current=0
            current+=value

            output=max(output, current)

        return output

    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(maxSubArray([5,4,-1,7,8]))
    print(maxSubArray([1]))
    print(maxSubArray([3,4,5,6,7,-999,234]))
    print(maxSubArray([3,4,5,6,7,-999,23]))
    print(maxSubArray([3,4,5,6,7,-9,26]))
    print(maxSubArray([-2,-1]))