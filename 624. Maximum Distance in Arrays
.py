class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        #keep track of 2 biggest NOT from the same arr
        greatest = float('-inf') ; second_greatest =  float('-inf')
        for arr in arrays:
            if arr[-1] > greatest:
                second_greatest = greatest
                greatest = arr[-1]
            elif arr[-1] > second_greatest:
                second_greatest = arr[-1]

        # second iteration to actually mark the difference
        res = 0
        for arr in arrays:
            n = len(arr) ; ele = greatest

            if greatest == arr[n-1]:
                ele = second_greatest
            res = max(res, ele - arr[0])
        
        return res
