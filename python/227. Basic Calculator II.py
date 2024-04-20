def calculate(s: str) -> int:
    stack=[]
    s = "".join(s.split()) #lebo kto by povedal ze v priklade su aj medzery

    i=0
    while i<len(s):
        if s[i]=="/" or s[i]=="*":
            u=i+1
            number=''
            while u< len(s) and s[u].isnumeric():
                number+= s[u]
                u+=1

            if s[i]=="*":
                stack.append(str(int(stack.pop()) * int(number)))
            elif s[i]=="/":
                stack.append(str(int(stack.pop()) // int(number)))

            i=u
            continue

        elif s[i] == "+" or s[i] == "-":
            stack.append(s[i])

        else:
            u=i
            number=''
            while u< len(s) and s[u].isnumeric():
                number += s[u]
                u+=1

            stack.append(number)
            i=u
            continue
        i+=1

    #return eval(''.join(stack))
    stack = stack[::-1]
    while len(stack)!=1:
        if stack[-2]=="+":
            stack[-1] = int(stack[-1]) + int(stack[-3])

        else:
            stack[-1] = int(stack[-1]) - int(stack[-3])
        stack.pop(-2)
        stack.pop(-2)


    return stack[0]



print(calculate(" 3/ 2 "))
print(calculate("3+2*2"))
print(calculate("3+2*25555"))
print(calculate("312+244*255"))
print(calculate("3+5/2"))
print("bordel")

print(calculate("312+244*255-2323*65653+213"))
print(calculate("31/2+24*255-23*63+213"))
print(calculate("31/2+24*255-23*0+0"))
print(calculate("31/2+24*255-0-23*0+0"))
print(calculate("0"))
