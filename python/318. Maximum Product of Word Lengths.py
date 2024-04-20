import itertools

class Solution:
    def maxProduct(self, words) -> int:
        maxis = 0
        for i, j in itertools.combinations(words, 2):
            if not set(i).intersection(j):  maxis = max(len(i)*len(j), maxis)

        return maxis

def main():
    sol = Solution()
    print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
    print(sol.maxProduct(["abcw","baz"]))
    print(sol.maxProduct(["abcw","kgz"]))

if __name__ == "__main__": main()