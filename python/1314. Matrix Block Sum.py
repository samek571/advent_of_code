class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
		
		#prefix sum
        prefix = mat[:][:]
        for i in range(m):
            for j in range(n):
                prefix[i][j] += (prefix[i-1][j] if i > 0 else 0) + \
                                (prefix[i][j-1] if j > 0 else 0) - \
                                (prefix[i-1][j-1] if i > 0 and j > 0 else 0)
		
		#block sum
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = prefix[min(i+k, m-1)][min(j+k, n-1)] + \
                               (prefix[i-k-1][j-k-1] if i-k > 0 and j-k > 0 else 0) - \
                               (prefix[i-k-1][min(j+k, n-1)] if i-k > 0 else 0) - \
                               (prefix[min(i+k, m-1)][j-k-1] if j-k > 0 else 0)
        
        return result
