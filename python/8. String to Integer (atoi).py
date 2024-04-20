class Solution:
    def myAtoi(s) -> int:
        s = s.strip()   #1. done
        number=''
        if len(s) == 0:
            return 0

        if len(s) == 1:
            if s[0].isdigit():
                return int(s)
            else:
                return 0

        if s[0] == '-':
            number += '-'
            s = s[1:]
            if not s[0].isdigit():
                return 0

        elif s[0] == '+':
            number += '+'
            s = s[1:]
            if not s[0].isdigit():
                return 0

        for i in s:
            try:
                i = int(i)
                i = str(i)
                number+=i
            except:
                break

        if len(number) == 0:
            return 0
        elif int(number) > 2**31 -1:
            number = 2**31 -1
        elif int(number) < -2**31:
            number = -2**31

        return int(number)

    print(myAtoi(""))