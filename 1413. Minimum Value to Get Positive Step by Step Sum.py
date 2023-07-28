class Solution:
    def minStartValue(nums) -> int:
        output=0
        value=0

        for number in nums:
            value+=number

            output=min(output,value)

        return abs(output)+1

    print(minStartValue([-3,2,-3,4,2]))
    print(minStartValue([1,2]))
    print(minStartValue([1,-2,-3]))