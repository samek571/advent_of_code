class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks: int) -> int:
        n = len(capacity)

        for i in range(n):
            capacity[i] -= rocks[i]

        capacity.sort()


        i = 0
        while i<n and additionalRocks >= 0:
            additionalRocks -= capacity[i]
            i+=1

        if additionalRocks<0: return i-1
        return i


def main():
    sol = Solution()
    print(sol.maximumBags([4,3], [2,1], 1)) #0
    print(sol.maximumBags([4,1], [2,1], 1)) #1
    print(sol.maximumBags([4], [2], 1)) #0
    print(sol.maximumBags([2,3,4,5], [1,2,4,4], 2)) #3

if __name__ == "__main__": main()
