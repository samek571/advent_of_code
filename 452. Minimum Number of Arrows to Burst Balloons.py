class Solution:
    def findMinArrowShots(points) -> int:
        if len(points)<2: return len(points)

        points = sorted(points, key=lambda x: x[0])

        start, end = 0, 1
        prev, curr = points[0], None
        conter=0
        for i in range(1, len(points)):
            curr = points[i]

            if curr[start] <= prev[end]: prev = [curr[start], min(curr[end],prev[end])]
            else:
                prev = curr
                conter+=1

        return conter+1

    print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
    print(findMinArrowShots([[1,1]]))
    print(findMinArrowShots([[1,3],[1,3]]))
    print(findMinArrowShots([[0,7],[1,3]]))