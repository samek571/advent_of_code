class Solution:
    def numberOfWays(self, n: int) -> int:
        n=n//2
        return (math.comb(2*n,n) // (n+1))%(10**9 + 7)
