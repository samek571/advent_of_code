class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        #think of it like simplier dijsktra
        nums = primes.copy()
        heapq.heapify(nums)
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums)

            for prime in primes:
                heapq.heappush(nums, p * prime)

                if p % prime == 0: break

        return p
