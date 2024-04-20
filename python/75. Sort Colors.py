import collections
import itertools
class Solution:
    def sortColors(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        numbers={0:0, 1:0, 2:0}
        #numbers=collections.Counter(nums)

        for i in range(n-1,-1,-1):
            numbers[nums[i]]+=1
            nums.pop()

        #it truly is just O(n)
        while len(nums)!=n:
            for key, val in numbers.items():
                for element in range(val):
                    nums.append(key)

        return nums

    print(sortColors([1,2,2,2,0,1,1,0]))
    print(sortColors([0]))
    print(sortColors([1]))
    print(sortColors([2,0,1]))
    print(sortColors([2,2,2,2,2,0,0,0,2,1,1,1,1,1,1,1,0,2,2,1,1,2,1]))


'''
1. count number of 2s and 0s --> O(n)

we go len(nums) and after encountering 0 --> i+=1
if we have witnessed all of the 0s we are allowed to repeat this process with
1s and 2s
'''