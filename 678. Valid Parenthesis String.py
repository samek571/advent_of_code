class Solution:
    def checkValidString(s: str) -> bool:
        lo = hi = 0

        for i in s:
            lo += 1 if i == '(' else -1
            hi += 1 if i != ')' else -1
            if hi < 0: return False
            lo = max(lo, 0)

        return lo == 0

    print(checkValidString("(()*(*)"))
    print(checkValidString("*****)"))
    print(checkValidString("***(*)"))
    print(checkValidString("((*)*(*)"))