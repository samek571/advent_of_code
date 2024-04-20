import copy
from collections import defaultdict

class Solution:
    def prisonAfterNDays(self, cells, n: int):# -> List[int]:
        # if cells == [0,0,0,1,1,0,1,0] and n == 574: return cells
        # if n%14==0: return ([0] + [1 ^ cells[i] for i in range(1, 7)] + [0])


        n %= 14
        if n==0: n=14
        while n: cells, n = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)] + [0], n-1
        return cells




def main():
    sol = Solution()
    print(sol.prisonAfterNDays([0,1,0,1,1,0,0,1], n = 7))
    print(sol.prisonAfterNDays([1,0,0,1,0,0,1,0], n = 1000000000))
    print(sol.prisonAfterNDays([1,1,0,1,1,0,0,1], 300663720))
    print(sol.prisonAfterNDays([0,0,0,1,1,0,1,0], 574))
    print(sol.prisonAfterNDays([0,0,1,1,0,1,0,1], 56))

if __name__ == "__main__": main()