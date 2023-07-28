import collections


class Solution:
    def countBadPairs(self, nums):# List[int]) -> int:
        seen, n, o = collections.defaultdict(int), len(nums), 0

        for idx, num in enumerate(nums):
            o+=seen[idx-num]
            seen[idx-num]+=1

        return n*(n-1)//2-o

def main():
    sol = Solution()
    print(sol.countBadPairs([4,1,3,3]))
    print(sol.countBadPairs([1,2,3,4,5]))

if __name__ == "__main__": main()