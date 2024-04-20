class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)

        if n + m != k:
            return False

        stack = [[0, 0, 0]]
        memo = set()
        while stack:
            a, b, c = stack.pop()
            if a == n and b == m and c == k:
                return True

            if (a, b) in memo:
                continue

            if a < n and s1[a] == s3[c]:
                stack.append([a + 1, b, c + 1])

            if b < m and s2[b] == s3[c]:
                stack.append([a, b + 1, c + 1])

            memo.add((a, b))

        return False
