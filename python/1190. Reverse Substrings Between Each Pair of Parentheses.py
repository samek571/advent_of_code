class Solution:
    def reverseParentheses(s: str) -> str:
        stack=[]

        for i in s:

            if i!=")": stack.append(i)
            else:
                temp=''
                while stack and stack[-1]!="(":
                    temp+= stack.pop()

                stack.pop()
                stack.append(temp[::-1])

        return "".join(stack[i][::-1] for i in range(len(stack)))

    print(reverseParentheses("(ed(et(oc))el)"))
    print(reverseParentheses("vdgzyj()"))
    print(reverseParentheses("((eqk((h))))"))
    print(reverseParentheses("(abcd)"))
    print(reverseParentheses("(u(love)i)"))
