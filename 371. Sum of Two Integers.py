class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a = bin(a).replace("0b", "")
        # b = bin(b).replace("0b", "")
        #
        #
        # return bin(sum(int(x, 2) for x in a))[2:]

        allll = (a,b)
        return sum(allll, 0)


def main():
    sol = Solution()
    print(sol.getSum(2,3))
    print(sol.getSum(1, 2))

if __name__ == "__main__": main()