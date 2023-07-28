class Solution:
    def isValid(s: str) -> bool:
        if len(s)%2==1:
            return False

        hovno=''
        for i in s:
            if len(hovno)==0 and (i==")" or i=="}" or i=="]"):
                return False

            if i == ")":
                if hovno[-1]=="(":
                    hovno=hovno[:-1]
                    continue
                elif hovno[-1]=="[" or hovno[-1]=="{":
                    return False

            elif i == "}":
                if hovno[-1]=="{":
                    hovno=hovno[:-1]
                    continue
                elif hovno[-1]=="[" or hovno[-1]=="(":
                    return False

            elif i == "]":
                if hovno[-1]=="[":
                    hovno=hovno[:-1]
                    continue
                elif hovno[-1]=="{" or hovno[-1]=="(":
                    return False

            else:
                hovno+=i

        if len(hovno)==0:
            return True
        else:
            return False

    print(isValid("{[)(]}"))
    print(isValid("]("))
    print(isValid("(){}}{"))
    print(isValid("[](]"))
    print(isValid("{[]}"))
    print(isValid("()[]{}"))
    print(isValid("([)]"))
    print(isValid("((}]"))
