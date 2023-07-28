class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        pos = -1
        mindist = float('inf')
        for i, (a, b) in enumerate(points):
            if a != x and b != y: continue
            dist = abs(x - a) + abs(y - b)
            if pos == -1 or dist < mindist:
                mindist = dist
                pos = i
        return pos
