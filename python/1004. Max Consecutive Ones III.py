class Solution:
    def longestOnes(nums, k: int) -> int:
        '''
        Find the first 1 (left pointer) and with right one go as far as possible, e.g skip k 0s
        highest = right-left+1

        start moving left towards right and after crossing through some 0, land
        on the closest 1. Start moving right pointer to the right and go through exactly the
        same number of 0 that has left pointer crossed on his road.
        Compare highest and r-l+1

        IF the number of consecutive zeroes along the way is greater
        than k -> let r find the closest 1 and let l=r. Then repeat the search over again

        End if the r=len(nums)

        '''
        l=r=maximus=0
        while r<len(nums):
            if nums[r] == 0:
                if k>0:
                    k-=1
                else:
                    maximus = max(maximus, r-l)
                    if nums[l] == 0:
                        k+=1
                    l+=1
                    continue
            r+=1

        return max(maximus, r-l)
    print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))
