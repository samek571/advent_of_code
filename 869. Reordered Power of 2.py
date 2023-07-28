from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))
        exp = 0
        j=len(str(n))

        while True:
            x=str(pow(2, exp))
            if len(x) > j: break

            if len(x) == j and Counter(x) == cnt: return True
            exp+=1


        return False


def main():
    sol = Solution()
    print(sol.reorderedPowerOf2(1))
    print(sol.reorderedPowerOf2(15))
    print(sol.reorderedPowerOf2(61))
    print(sol.reorderedPowerOf2(46))
    print(sol.reorderedPowerOf2(8219))
    print(sol.reorderedPowerOf2(8129))
    print(sol.reorderedPowerOf2(10))

if __name__ == "__main__": main()
