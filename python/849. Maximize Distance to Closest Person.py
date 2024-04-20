class Solution:
    def maxDistToClosest(seats) -> int:
        n = len(seats)
        empty, result, left, right = 0, 0, -1, -1

        for i in range(n):
            if seats[i] == 1:
                empty = 0
                if left == -1: left = i
                right = i
            else:
                empty += 1
                result = max(result, (empty + 1) // 2)

        return max(result, left, n - 1 - right)


    print(maxDistToClosest([1,0,0,1]))
    print(maxDistToClosest([1,0,0,0]))
    print(maxDistToClosest([1,0,0,0,1,0,1]))
    print(maxDistToClosest([0,0,1,0,0,0,1,0,1]))

