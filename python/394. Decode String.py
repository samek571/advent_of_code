class Solution:
    def decodeString(s: str) -> str:
        stack=[]

        for i in s:
            if i!="]": stack.append(i)
            else:
                answer=''
                while stack[-1] != "[":
                    answer=stack.pop()+answer

                stack.pop()
                num=''
                while len(stack)>0 and stack[-1].isnumeric():
                    num=stack.pop()+num

                # answer = answer[::-1]
                # num=num[::-1]
                stack.append(int(num)* answer)

        return ''.join(stack)


    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))
    print(decodeString("2[abc]3[cd]ef" ))
    print(decodeString("abc3[cd]xyz"))

    print("\n")
    print(decodeString("abc10[cd]xyz"))
    print(decodeString("3[a2[c]]hh"))
    print(decodeString("3[a2[c]]hh5[y]"))
    print(decodeString("a2[3[b2[c]]]"))
    print(decodeString("a1[3[b2[c]uuuuud]iudfbisdhsidf]hh5[yh]p"))
