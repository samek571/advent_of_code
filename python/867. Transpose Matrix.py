class Solution:
    def transpose(self, x: List[List[int]]) -> List[List[int]]:
        return [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
