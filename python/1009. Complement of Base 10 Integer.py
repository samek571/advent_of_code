class Solution:
    def findComplement(n: int) -> int:
        return n ^ int('1' * len(bin(n)[2:]), 2)
