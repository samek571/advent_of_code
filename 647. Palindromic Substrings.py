class Solution:
    def countSubstrings(self, s: str) -> int:

        def do(s, l, r):

            amount = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                amount+=1
                l-=1
                r+=1

            return amount

        total = 0
        for i in range(len(s)):
            total += do(s, i, i+1)

        for i in range(len(s)):
            total += do(s, i, i)

        #return '\"' + s + '\"'
        return total

def main():
    sol = Solution()
    print(sol.countSubstrings("agatamasamataga"))
    print(sol.countSubstrings("aaaaaaaaaa")) #10
    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("watta"))
    print(sol.countSubstrings("akka"))
    print(sol.countSubstrings("aka"))
    print(sol.countSubstrings("g"))

if __name__ == "__main__": main()
