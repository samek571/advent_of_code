class Solution:
    def islandPerimeter(grid) -> int:
        m, n = len(grid), len(grid[0])
        output = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    output += 4
                    if i > 0 and grid[i - 1][j]:
                        output -= 2
                    if j > 0 and grid[i][j - 1]:
                        output -= 2
        return output

    print(islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0], [1,0,0,0]]))
    print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(islandPerimeter([[4]]))
    print(islandPerimeter([[1,0],[0,1]]))
    print(islandPerimeter([[1,0]]))

# class Solution:
#     def islandPerimeter(grid) -> int:
#         #1x1
#         if len(grid)==len(grid[0])==1:
#             if grid[0][0]==1:
#                 return 4
#             else:
#                 return 0
#
#         #1xn
#         elif len(grid)==1 and len(grid[0])>1:
#             for i in range(1,len(grid[0]-1):
#                 if grid[0][i]==1 and
#
#         number_of_ones=0
#         tangent_area=0
#
#         #works for 2x2 at least
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]== 1:
#                     number_of_ones+=1
#
#                     #not edges
#                     if i!=0 and j!=0 and i!=len(grid)-1 and j!=len(grid[0])-1:
#                         #print(grid[i][j], i, j)
#                         if grid[i][j-1]==1:
#                             tangent_area+=1
#                         if grid[i-1][j]==1:
#                             tangent_area+=1
#                         if grid[i][j+1]==1:
#                             tangent_area+=1
#                         if grid[i+1][j]==1:
#                             tangent_area+=1
#
#                     else:
#                         #horne bez rohov
#                         if i==0 and j!=0 and j!=len(grid[0])-1:
#                             if grid[i][j-1]==1:
#                                 tangent_area+=1
#                             if grid[i][j+1]==1:
#                                 tangent_area+=1
#                             if grid[i+1][j]==1:
#                                 tangent_area+=1
#
#                         #dolne bez rohov
#                         elif i==len(grid)-1 and j!=0 and j!=len(grid[0])-1:
#                             if grid[i][j-1]==1:
#                                 tangent_area+=1
#                             if grid[i-1][j]==1:
#                                 tangent_area+=1
#                             if grid[i][j+1]==1:
#                                 tangent_area+=1
#
#                         # prave bez rohov
#                         elif j==len(grid)-1 and i!=0 and i!=len(grid)-1:
#                             if grid[i][j-1]==1:
#                                 tangent_area+=1
#                             if grid[i-1][j]==1:
#                                 tangent_area+=1
#                             if grid[i+1][j]==1:
#                                 tangent_area+=1
#
#                         #lave bez rohov
#                         elif j==0 and i!=0 and i!=len(grid)-1:
#                             if grid[i-1][j]==1:
#                                 tangent_area+=1
#                             if grid[i][j+1]==1:
#                                 tangent_area+=1
#                             if grid[i+1][j]==1:
#                                 tangent_area+=1
#
#                         #lavyhorny
#                         elif j==i==0:
#                             if grid[i][j+1]==1:
#                                 tangent_area+=1
#                             if grid[i+1][j]==1:
#                                 tangent_area+=1
#
#                         #pravydolny
#                         elif j==i==len(grid)-1:
#                             if grid[i][j-1]==1:
#                                 tangent_area+=1
#                             if grid[i-1][j]==1:
#                                 tangent_area+=1
#
#                         #lavydolny
#                         elif j==0 and i==len(grid)-1:
#                             if grid[i][j+1]==1:
#                                 tangent_area+=1
#                             if grid[i-1][j]==1:
#                                 tangent_area+=1
#
#                         #pravyhorny
#                         elif j==len(grid)-1 and i==0:
#                             if grid[i+1][j]==1:
#                                 tangent_area+=1
#                             if grid[i][j-1]==1:
#                                 tangent_area+=1
#
#         return number_of_ones*4-tangent_area

