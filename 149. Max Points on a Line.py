from collections import defaultdict

class Solution:
    def maxPoints(self, points) -> int:
        n = len(points)
        if n == 1: return 1

        output = 1
        for i in range(n):
            dick = defaultdict(int)
            x1, y1 = points[i][0], points[i][-1]
            for j in range(i+1, n):
                x, y = points[j][0]-x1, points[j][-1]-y1

                if x == 0: s = float("inf")
                else: s = y / x


                dick[s] += 1
                output = max(output, dick[s])

        return output+1



def main():
    sol = Solution()
    print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

if __name__ == "__main__": main()


# class Solution:
#     def maxPoints(self, points) -> int:
#         n = len(points)
#         if n == 1: return n
#
#
#         dick = defaultdict(list)
#         for point1 in points:
#             for point2 in points:
#                 if point1 == point2: continue
#
#                 y_delta, x_delta = (point2[0] - point1[0]), (point2[-1]-point1[-1])
#
#                 if x_delta == 0: s = float("inf")
#                 else: s = y_delta / x_delta
#
#
#                 dick[s].append(point1)
#
#         print(dick)
#         maxlenght = 0
#
#         for key, val in dick.items():
#             maxlenght = max(maxlenght, len(val)//2)
#
#         return maxlenght