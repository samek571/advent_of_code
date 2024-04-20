class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        flag=True
        d = arr[1]-arr[0]
        for i in range(1, len(arr)):
            if d != arr[i]-arr[i-1]: 
                flag=False
                break
        
        return flag
