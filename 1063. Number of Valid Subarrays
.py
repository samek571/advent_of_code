class Solution:
    def validSubarrays(self, arr: List[int]) -> int:
        s = [] ; res = [0] * len(arr)
        
        for i, n in enumerate(arr + [-1]):
            while s and n < arr[s[-1]]:
                j = s.pop()
                res[j] += i - j
            
            s.append(i)
        
        
        return sum(res)
