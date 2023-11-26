class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        nums.append(k)
        i, res, window_sum = 0, 0, 0

        for j in range(len(nums)):
            window_sum += nums[j]

            #shrinking window
            while window_sum * (j-i+1) >= k:
                res += j-i # amount of valid subarrays, for lenght 4 it is 1+1+1+1 for each lenght from 1 to 4
                window_sum -= nums[i]
                i+=1 #maybe there is a gap that could be extended further, lets explore that

        return res
