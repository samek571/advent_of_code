class Solution:
    '''the point is to start at lowest numbers since if we lack these there is not way we gonna cover up by adding greater
    therefore check if there is 1, then if there is 2, if so make a prefix sum and if that is greater than the next element in aray its okay if not its the results we aregoning to increase by one and "double the prefix sum +1" since we add the next greater lacking numebr that can not be reach by the sum of the array'''
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0 ; pre = 0
        
        for i in range(len(nums)):
            while pre < nums[i]-1 and pre < n:
                pre += pre + 1 #adding the next greater element to prefixsum == double+1
                ans += 1 #since we added one number
            
            pre += nums[i] #doing prefixsum
            
            if pre >= n: break #understandably reached the end
        

        #since sometimes just the n is mega big we dont need to verify the integrity of last element in arr
        while pre < n:
            pre += pre + 1
            ans += 1
        

        return ans
