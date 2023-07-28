class Solution:
    def matrixReshape(self, matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
        R,C = len(matrix), len(matrix[0])
        
        if R*C!=r*c: return matrix

        output = []
        tmp=[]
        for i in range(R):
            for j in range(C):
                tmp.append(matrix[i][j])
                if len(tmp) == c:
                    output.append(tmp)
                    tmp=[]
        
        return output
