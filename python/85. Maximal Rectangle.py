#had this shit in school
class Solution:

    #my 84
    def leetcode84(self, heights):
        s = []
        max_area = 0
        idx = 0

        while idx < len(heights):
            if not s or heights[s[-1]] <= heights[idx]:
                s.append(idx)
                idx += 1
            else:
                top_of_stack = s.pop()
                area = (heights[top_of_stack] * ((idx - s[-1] - 1) if s else idx))
                max_area = max(max_area, area)

        while s:
            top_of_stack = s.pop()
            area = (heights[top_of_stack] * ((idx - s[-1] - 1) if s else idx))
            max_area = max(max_area, area)

        return max_area



    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        maxarea = 0
        #2d prefixsum
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea
