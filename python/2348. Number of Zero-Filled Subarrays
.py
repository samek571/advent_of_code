class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        o, i, tmp = 0, 0, 0
        while i < len(nums):
            if nums[i] ==0:
                tmp+=1
            else:
                o += (tmp*(tmp+1)) //2
                tmp=0
            i+=1

        return o + (tmp*(tmp+1)) //2
