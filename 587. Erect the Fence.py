class Solution:
    # graham scan algo
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort(key=lambda p: (p[0], p[1]))

        def orientation(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def computeConvexHull(points: List[List[int]]) -> List[List[int]]:
            n = len(points)
            if n < 3:
                return points

            hull = []
            hull.append(points[0])
            hull.append(points[1])

            for i in range(2, n):
                while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) > 0:
                    hull.pop()
                hull.append(points[i])

            return hull

        # left to right and back
        upper_hull = computeConvexHull(trees)
        lower_hull = computeConvexHull(trees[::-1])
        outer_boundary = list(set(map(tuple, upper_hull + lower_hull)))

        return [list(point) for point in outer_boundary]