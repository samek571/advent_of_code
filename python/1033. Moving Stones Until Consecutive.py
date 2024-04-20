class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        a, b, c = sorted([a,b,c])
        if a+1 == b == c-1: return [0,0]

        def minimalus(a,b,c):
            if a+1==b or b+1 == c or c-b==2 or b-a==2: return 1
            else: return 2

        def maximalus(a,c):
            return c-a-2

        return [minimalus(a,b,c), maximalus(a,c)]

def main():
    sol = Solution()
    print(sol.numMovesStones(1,7,28))
    print(sol.numMovesStones(-111,7,28))
    print("###############################")
    print(sol.numMovesStones(1,2,5))
    print(sol.numMovesStones(4,3,2))
    print(sol.numMovesStones(3,5,1))

if __name__ == "__main__": main()