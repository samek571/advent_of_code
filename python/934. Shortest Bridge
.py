class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        q = [] ; n = len(grid); res=0
        def dfs(x,y):
            
            q.append([x,y])
            grid[x][y] = -1

            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(grid) and grid[i + x][j + y] == 1:
                    dfs(i + x, j + y)




        def bfs(x, y, island):
            queue = [[x, y]]
            visited = set([(x, y)])
            distance = 0

            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.pop(0)

                    if grid[node[0]][node[1]] == 1 and (node[0], node[1]) not in island:
                        return distance - 1

                    for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        new_x, new_y = node[0] + i, node[1] + j
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid) and (new_x, new_y) not in visited:
                            queue.append([new_x, new_y])
                            visited.add((new_x, new_y))

                distance += 1

            return -1



        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break


        
        while q:
            for _ in range(len(q)):
                i,j = q.pop(0)
                
                for x,y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    xi,yj = x+i,y+j
                    if 0<=xi<n and 0<=yj<n and grid[xi][yj] != -1:
                        if grid[xi][yj] == 1:
                            return res
                        
                        elif grid[xi][yj] == 0:
                            q.append((xi,yj))
                            grid[xi][yj] = -1
            res+=1                

        return res-1

