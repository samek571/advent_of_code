class Solution:
    def numDistinctIslands2(self, mat: List[List[int]]) -> int:

        allDistinctIslands = set()
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                # if island
                if mat[r][c] == 1:
                    positions = []
                    self.getIsland(mat, r, c, positions)
                    allDistanceCountMap = {}
                    
                    #lets say its constant since the size of the island isnt big by default
                    # the trick here is being done by measuring distance of 2 points using pythagorean theorem 
                    for i in range(len(positions)):
                        for j in range(i + 1, len(positions)):
                            # no need to sqrt since its just a constant for each and every ij
                            dist = (positions[i][0] - positions[j][0]) ** 2 + (positions[i][1] - positions[j][1]) ** 2
                            allDistanceCountMap[dist] = allDistanceCountMap.get(dist, 0) + 1
                    
                    # we are asked the number of different island
                    allDistinctIslands.add(frozenset(allDistanceCountMap.items()))
        
        
        return len(allDistinctIslands)


    #make a dfs to find the whole island as it is
    def getIsland(self, mat: List[List[int]], r: int, c: int, positions: List[List[int]]):
        positions.append([r, c])
        mat[r][c] = 0 # in place marking and anticycling measure
        
        for x,y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            rNext, cNext = r+x, c+y
            
            if rNext < 0 or rNext >= len(mat) or cNext < 0 or cNext >= len(mat[0]) or mat[rNext][cNext] == 0: continue
            
            self.getIsland(mat, rNext, cNext, positions)
