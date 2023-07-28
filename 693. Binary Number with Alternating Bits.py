class Solution:
    def hasAlternatingBits(n: int) -> bool:
        n=bin(n)[2:]

        for i in range(1, len(n)):
            if n[i-1] == n[i]: return False

        return True


    print(hasAlternatingBits(1))
    print(hasAlternatingBits(2))
    print(hasAlternatingBits(22))
    print("")
    print(hasAlternatingBits(11))
    print(hasAlternatingBits(7))
    print(hasAlternatingBits(5))