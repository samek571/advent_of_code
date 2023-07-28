import heapq


class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        piles = [-i for i in piles]

        heapq.heapify(piles)
        for _ in range(k):
            #print(piles)

            # it needs to be [0] cuz its queue !!
            # therefore we are rotating the whole array by doing -1*element
            heapq.heapreplace(piles, piles[0]//2)

        # accordingly -1*sum cuz we made a reverse sort basically
        return -sum(piles)



def main():
    sol = Solution()
    print(sol.minStoneSum(piles = [5,4,9], k = 2))
    print(sol.minStoneSum(piles = [4,3,6,7], k = 3))

if __name__ == "__main__": main()
