class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        modula = 10**9 + 7 ; numRow, numCol = len(pizza), len(pizza[0])
        
        #prefix
        mat = [[0] * (numCol+1) for _ in range(numRow+1)]
        for r in range(numRow):
            for c in range(numCol):
                mat[r+1][c+1] = mat[r][c+1] + mat[r+1][c] - mat[r][c] + (1 if pizza[r][c] == 'A' else 0)
        
        #using prefix calcutaes the number of apples efficiently, used in dfs - decision making
        count = lambda r1, c1, r2, c2: mat[r2+1][c2+1] - mat[r2+1][c1] - mat[r1][c2+1] + mat[r1][c1]
        

        @cache
        def dfs(r, c, cut):
            if count(r, c, numRow-1, numCol-1) < k - cut: return 0
            elif cut == k-1: return 1
            sub = 0
            for i in range(r, numRow):
                if count(r, c, i, numCol-1) > 0:
                    sub += dfs(i+1, c, cut+1)
                    if sub >= modula: sub %= modula
            for j in range(c, numCol):
                if count(r, c, numRow-1, j) > 0:
                    sub += dfs(r, j+1, cut+1)
                    if sub >= modula: sub %= modula
            return sub
        
        
        return dfs(0, 0, 0)
