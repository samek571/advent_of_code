class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        o, R,C = 0, len(strs), len(strs[0])


        for j in range(C):
            for i in range(1,R):

                if strs[i][j] < strs[i-1][j]: 
                    o+=1
                    break
        
        return o


        # could have been done with sort that has O(n) best and O(nlogn) (patience s. for example)
        # it would be a lil slower tho
