import collections
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)  # which quadrant we consider
        if x > y: x, y = y, x

        seen={(0,0)}
        q = collections.deque([[0, 0, 0]])
        while q:
            i, j, cnt = q.popleft()
            if i == x and j == y: return cnt

            for r, s in [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]:
                if (i + r, j+s) not in seen:
                    q.append([i + r, j + s, cnt + 1])
                    seen.add((i + r, j+s))

        return cnt


def main():
    sol = Solution()
    print(sol.minKnightMoves(5,5))
    print(sol.minKnightMoves(1,0))
    print(sol.minKnightMoves(2,112))

if __name__ == "__main__": main()
