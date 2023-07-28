class Solution:
    def maxWidthOfVerticalArea(points) -> int:
        points.sort(key=lambda x: x[0])

        maximal=0
        for i in range(1, len(points)):
            maximal = max(maximal, points[i][0] - points[i-1][0])

        return maximal


    print(maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
    print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
    print(maxWidthOfVerticalArea([[1,2],[2,2],[3,2],[4,2],[5,2]]))
    print(maxWidthOfVerticalArea([[1,2],[1,2],[3,2],[4,2],[5,2]]))
    print(maxWidthOfVerticalArea([[1,2],[1,2],[1,2],[1,2],[1,2]]))