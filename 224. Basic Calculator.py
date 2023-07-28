class Solution:
    def calculate(s: str) -> int:
        s = "".join(s.split())
        #return eval(s)

        num = 0
        res = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit(): num = 10*num + int(char)

            elif char in {"-", "+"}:
                res += num*sign
                num = 0
                if char == "-": sign = -1
                else: sign = 1

            elif char == "(":
                stack.append(res)
                res = 0
                stack.append(sign)
                sign = 1

            elif char == ")":
                res += num*sign
                res *= stack.pop()
                res += stack.pop()
                num = 0

        return res + num * sign

    print(calculate("(1-(4+5+2)-3)+(6+8)"))
    print(calculate("1+0-(1+7)"))
    print(calculate("1+0-1"))

    print("testaces")
    print(calculate("1 + 1"))
    print(calculate("(1+(4+5+2)-3)+(6+8)"))
    print(calculate(" 2-1 + 2 "))

        # stack=[]
        # i=0
        # while i<(len(s)):
        #     if s[i].isnumeric():
        #         u = i
        #         number = ''
        #         while u < len(s) and s[u].isnumeric():
        #             number += s[u]
        #             u += 1
        #
        #         if len(stack)>=2 and stack[-1] in {"+", "-"} and stack[-2].isnumeric():
        #             if stack[-1]=="-":
        #                 stack[-2] = str(int(stack[-2]) - int(number))
        #                 stack.pop()
        #             else:
        #                 stack[-2] = str(int(stack[-2]) + int(number))
        #                 stack.pop()
        #         else: stack.append(number)
        #         i = u
        #         continue
        #
        #     elif s[i] == ")":
        #         number = stack.pop()
        #         stack.pop()
        #
        #         if len(stack)==0:
        #             stack.append(number)
        #
        #         else:
        #
        #             if stack[-1] == "+": stack.append(number)
        #             elif stack[-1] == "-": stack.append(str(-1* int(number)))
        #
        #             while len(stack)>=3 and stack[-2] in {"+", "-"} and stack[-3].isnumeric():
        #                 if stack[-2] == "+": temp = str(int(stack[-1]) + int(stack[-3]))
        #                 else: temp = str(int(stack[-1]) - int(stack[-3]))
        #                 stack.pop()
        #                 stack.pop()
        #                 stack[-1] = temp
        #
        #             # if len(stack)==2 and stack[0] == "(":
        #             #     number = stack.pop()
        #             #     stack.pop()
        #             #     stack.append(number)
        #
        #             i+=1
        #             continue
        #
        #     else:
        #         stack.append(s[i])
        #
        #     i+=1
        #
        # return stack[-1]
