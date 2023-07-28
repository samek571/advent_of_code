import collections


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        hsh = collections.defaultdict(int)
        hsh[0]=1

        prefix = 0
        o = 0

        for num in nums:
            prefix+=num

            if prefix-k in hsh:
                o += hsh[prefix-k]

            hsh[prefix] +=1

        return o

def main():
    sol = Solution()
    print(sol.subarraySum([1,2,3, 0, 0 , -2, 3], 3))
    print(sol.subarraySum([1,2,3, 0, 0 , -1, 3], 3))
    print(sol.subarraySum([1,2,3], 3))

if __name__ == "__main__": main()
