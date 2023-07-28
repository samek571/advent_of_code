class Solution:
    def minAddToMakeValid(s: str) -> int:
        # stack=''
        #
        # for i in s:
        #     if len(stack)>0 and stack[-1] == "(" and i == ")": stack = stack[:-1]
        #     else: stack+=i
        #
        # return len(stack)

        stack=[]
        for i in s:
            if stack and stack[-1] == "(" and i == ")": stack.pop()
            else: stack+=i

        return len(stack)

    print(minAddToMakeValid("())"))
    print(minAddToMakeValid("((("))
    print(minAddToMakeValid("()"))
    print(minAddToMakeValid("()))(("))
    print("")
    print(minAddToMakeValid("((()()())"))
