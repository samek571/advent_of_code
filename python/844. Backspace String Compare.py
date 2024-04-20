class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_stack = ''
        t_stack = ''

        for i in s:
            if i == "#": s_stack = s_stack[:-1]
            else: s_stack+=i

        for i in t:
            if i == "#": t_stack = t_stack[:-1]
            else: t_stack+=i

        return t_stack is s_stack



def main():
    sol = Solution()
    print(sol.backspaceCompare("ad#c", "ab#c"))
    print(sol.backspaceCompare("a#b", "b"))

if __name__ == "__main__": main()