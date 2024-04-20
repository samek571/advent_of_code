import collections
import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        # O(n^2)
        # m = []
        # heapq.heapify(m)

        # for row in matrix:
        #     for element in row:
        #         heapq.heappush(m, element)

        # return heapq.nsmallest(k, m)[-1]

        # all the 0indexed get in pq and then lowest gets popped and next falls in line
        pq = []
        heapq.heapify(pq)

        for i, arr in enumerate(matrix):
            matrix[i] = collections.deque(arr)
            heapq.heappush(pq, (matrix[i].popleft(), i))

        print(pq)

        while k > 1:
            num, i = heapq.heappop(pq)

            if matrix[i]:
                heapq.heappush(pq, (matrix[i].popleft(), i))
            k -= 1

        return heapq.heappop(pq)[0]


def main():
    sol = Solution()
    print(sol.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8))

if __name__ == "__main__": main()
