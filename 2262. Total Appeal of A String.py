import collections


class Solution:
    def appealSum(self, s: str) -> int:
        output, n, hsh =0, len(s), collections.defaultdict(lambda : -1)

        for i, ch in enumerate(s):

            output+= (n-i)*(i-hsh[ch])
            hsh[ch]=i

        return output


def main():
    sol = Solution()
    print(sol.appealSum("abbca"))
    print(sol.appealSum('abcba'))
    print(sol.appealSum('abcab'))
    print(sol.appealSum('cpde'))

    print(sol.appealSum('abc'))
    print(sol.appealSum('aba'))
    print(sol.appealSum('leetcode'))

if __name__ == "__main__": main()
