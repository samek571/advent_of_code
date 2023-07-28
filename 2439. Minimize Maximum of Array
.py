class Solution:
    '''we have reversly sorted array in the end, the only limitation we are facing is that the 0th element cannot be decreased therefore its our first shoot. If more trouble occur like 
    5, 2, 19 we need to distribute the 19 as equaly as possible - leaving us with 9,9,8 since is the lowest we can get. Therefore for each next element we look if it isnt a threat like the 19 in this case, otherwise the already discovered maximum stays'''
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        ans=0 ; s=0
        for i in range(len(nums)):
            s+=nums[i]
            ans=max(ans,(s+i)//(i+1))
        return ans
