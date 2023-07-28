class Solution:
    def countAndSay(self, n) -> str:

        actual='1'


        for i in range(1, n):

            strike=1
            new=''
            for idx in range(1, len(actual)):

                if actual[idx] != actual[idx-1]:
                    new += str(strike) + actual[idx-1]
                    strike=1

                else:
                    strike+=1

            new += str(strike) + actual[-1]
            actual = new


        return actual
                


def main():
    sol = Solution()
    print(sol.countAndSay(6)) #"312211"
    print(sol.countAndSay(5)) #"111221"
    print(sol.countAndSay(4))

if __name__ == "__main__": main()