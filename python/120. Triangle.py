class Solution:
    def minimumTotal(triangle) -> int:
        # if len(triangle)<3:
        #     if len(triangle) == 2: return triangle[0][0] + min(triangle[1][0], triangle[1][1])
        #     else: return triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

        return min(triangle[-1])

    print(minimumTotal([[2]]))
    print(minimumTotal([[2],[2,3]]))
    print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))