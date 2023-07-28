class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums  = [str(i) for i in nums]


        #custom bubbel sorter        
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                a,b=nums[j], nums[j+1]

                if int(a+b) < int(b+a):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        #fucking edge case
        if nums[0] == "0": return '0'

        return ''.join(nums)
