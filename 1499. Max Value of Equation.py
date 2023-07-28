import heapq

class Solution:
    '''
    sliding window which is dequeue in this case

    While we havent reached the end:
    - appending till the difference of xi - x0 <= k. thats some number of satisfying partners for the leftmost element
    --> we go through them all and mark the greatest result | O(n^2)
    - if the difference is greater, the leftmost gets popped

    optimization is by doing heapq
    '''
    def findMaxValueOfEquation(self, points, k: int) -> int:

        ret = float('-inf')
        pq = []
        heapq.heapify(pq)

        for [x, y] in points:
            while pq and x - pq[0][1] > k: heapq.heappop(pq)
            if pq:
                eq = x + y - pq[0][0]
                ret = max(eq, ret)
            heapq.heappush(pq, (x - y, x))

        return ret

def main():
    sol = Solution()
    print(sol.findMaxValueOfEquation(points = [[-17,-6],[-4,0],[-2,-16],[-1,2],[0,11],[6,18]], k = 13)) #35
    print(sol.findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]], k = 1))
    print(sol.findMaxValueOfEquation([[0,0],[3,0],[9,2]], k = 3))
    print(sol.findMaxValueOfEquation([[0,0],[3,0]], k = 3))
    print(sol.findMaxValueOfEquation([[0,0],[3,0]], k = 2))

if __name__ == "__main__": main()

        # ret = -float('inf')
        # window = deque([]);
        # points = deque(points)
        # print(window, points)
        #
        # while points:
        #     if not window:
        #         window.append(points.popleft())
        #
        #     while points and points[0][0] - window[0][0] <= k:
        #         window.append(points.popleft())
        #
        #     i, j = window.popleft()
        #     for x, y in window:
        #         ret = max(ret, y + j + abs(x - i))
        #
        # while len(window) >= 2:
        #     i, j = window.popleft()
        #     for x, y in window:
        #         ret = max(ret, y + j + abs(x - i))
        #
        # return ret
