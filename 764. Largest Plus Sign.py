import collections


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines) -> int:
        dp, ans = [[0] * n for _ in range(n)], 0
        banned = {tuple(mine) for mine in mines}

        for i in range(n):
            count = 0
            for j in range(n):
                count = count + 1 if (i, j) not in banned else 0
                dp[i][j] = count

            count = 0
            for j in range(n - 1, -1, -1):
                count = count + 1 if (i, j) not in banned else 0
                dp[i][j] = min(dp[i][j], count)

        for j in range(n):
            count = 0
            for i in range(n):
                count = count + 1 if (i, j) not in banned else 0
                dp[i][j] = min(dp[i][j], count)

            count = 0
            for i in range(n - 1, -1, -1):
                count = count + 1 if (i, j) not in banned else 0
                dp[i][j] = min(dp[i][j], count)
                ans = max(ans, dp[i][j])

        return ans


def main():
    sol = Solution()
    print(sol.orderOfLargestPlusSign(5, [[4,2], [4,3], [3,4]]))
    print(sol.orderOfLargestPlusSign(5, [[4,2]]))
    print(sol.orderOfLargestPlusSign(5, []))
    print(sol.orderOfLargestPlusSign(2, [[0,0], [1,1], [0,1], [1,0]]))
    print(sol.orderOfLargestPlusSign(2, [[0,0], [1,1], [0,1] ]))
    print(sol.orderOfLargestPlusSign(3, [[0,0], [1,1], [0,1] ]))
    print(sol.orderOfLargestPlusSign(3, [[0,0], [2,2]]))
    print(sol.orderOfLargestPlusSign(1, [[0,0]]))

if __name__ == "__main__": main()

'''
        l = len(mines)
        if n == 1 or n**2 == l:
            return 0

        xhsh=collections.defaultdict(list)
        yhsh=collections.defaultdict(list)
        for x,y in mines:
            xhsh[x].append(y)
            yhsh[y].append(x)

        o=1
        for x in range(n):
            for y in range(n):

                xmin=n
                if x in xhsh:
                    for i in xhsh[x]:
                        xmin = min(xmin, abs(i-y))

                ymin=n
                if y in yhsh:
                    for i in yhsh[y]:
                        ymin = min(ymin, abs(i-x))

                tmp = min(ymin, xmin, y+1, x+1, n-y, n-x)
                o = max(tmp, o)

        return o

'''