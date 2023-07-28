class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        r, choices = 0, sorted([(num1^(1<<i)) - num1 for i in range(32)])

        while num2:
            while not num2 & 1:
                num2>>=1
            num2>>=1
            r += abs(choices.pop(0))

        return r
