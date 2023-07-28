class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        if len(pairs)<2: return len(pairs)

        points = sorted(pairs, key=lambda x: x[0])

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
