import math


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        x=columnNumber//26
        y=columnNumber%26

        if y==0: x-=1; y=26

        s=chr(64+y)
        while x>0:
            y=x%26

            if y==0: x-=1 ; y=26

            x//=26
            s+=chr(64+y)


        return s[::-1]


def main():
    sol = Solution()
    print(sol.convertToTitle(701)) #ZY
    print(sol.convertToTitle(702)) #ZZ
    print(sol.convertToTitle(1)) #A
    print(sol.convertToTitle(28)) #AB
    print(sol.convertToTitle(18278)) #ZZZ
    print(sol.convertToTitle(18279)) #AAAA
    print(sol.convertToTitle(52)) #AZ
    print(sol.convertToTitle(53)) #BA

if __name__ == "__main__": main()