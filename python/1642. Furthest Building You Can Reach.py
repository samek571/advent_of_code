import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        if not ladders and not bricks and n>1:
            j=1
            while heights[j]<=heights[j-1]:
                j+=1

            return j-1


        pq = [] ; soFarSum = 0
        heapq.heapify(pq)

        for i in range(1, n):
            delta = heights[i]-heights[i-1]

            if delta > 0:
                if len(pq)==ladders and pq:
                    smallestLadder = heapq.heappop(pq)

                    soFarSum += min(delta, smallestLadder)
                    heapq.heappush(pq, max(delta, smallestLadder))

                elif ladders>0: heapq.heappush(pq, delta)

            #else moves without any difficulties

            if soFarSum > bricks: return i-1


        return len(heights)-1


def main():
    sol = Solution()
    print(sol.furthestBuilding([1,2], 0, 0))
    print(sol.furthestBuilding([1], 0, 0))
    print(sol.furthestBuilding([12,10,7,5,3,3,2,7], 0, 0))
    print(sol.furthestBuilding([1,2], 1, 0))
    print(sol.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
    print(sol.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
    print(sol.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))

if __name__ == "__main__": main()