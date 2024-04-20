class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt=0
        punish, s = [], list(s)

        for i in range(len(s)):
            if cnt == 0 and s[i] == ")": s[i]= ""
            elif s[i] == ")":
                cnt-=1
                punish.pop()
            elif s[i] == "(":
                cnt+=1
                punish.append(i)

        for i in punish:
            s[i] = ""


        return "".join(s)





def main():
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sol.minRemoveToMakeValid("a)b(c)d"))
    print(sol.minRemoveToMakeValid("(())"))
    print(sol.minRemoveToMakeValid("))(("))

if __name__ == "__main__": main()