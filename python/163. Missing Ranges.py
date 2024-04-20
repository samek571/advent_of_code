class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]

        o=[]
        for i in range(1, len(nums)):
            fate = nums[i] - nums[i-1]
            
            if fate > 1:
                if fate == 2: o.append(str(nums[i-1]+1))
                else: o.append(str(nums[i-1]+1) + "->" + str(nums[i]-1))

        return o


        
