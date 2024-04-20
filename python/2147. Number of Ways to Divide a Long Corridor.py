class Solution:
    def numberOfWays(self, corridor: str) -> int:

        #we are interested only in the seats
        possibilities = [idx for idx in range(len(corridor)) if corridor[idx] == "S"]

        #filter the shit right away
        l = len(possibilities)
        if not l or l % 2:
            return 0

        #considering just the distance inbetween 2 seats
        res = 1
        mod = 10**9 + 7
        for idx in range(l//2 - 1):
            res = (res * (possibilities[2*idx+2] - possibilities[2*idx+1])) % mod

        return res
