import collections

class Solution:
    def findJudge(self, n: int, trust):# List[List[int]]) -> int:
        trusts, is_trusted = set(), collections.defaultdict(int)

        for a,b in trust:
            trusts.add(a)
            is_trusted[b]+=1

        for i in range(1, n+1):
            if i not in trusts and is_trusted[i] == n-1: return i

        return -1


def main():
    sol = Solution()
    print(sol.findJudge(2, trust = [[1,2]]))
    print(sol.findJudge(3, [[1,3],[2,3]]))
    print(sol.findJudge(3, [[1,3],[2,3],[3,1]]))

if __name__ == "__main__": main()
