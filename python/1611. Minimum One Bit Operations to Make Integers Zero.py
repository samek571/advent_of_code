class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n==0: return 0
        return n ^ self.minimumOneBitOperations(n>>1)
        #rightmost bit set changed by xor in each level, same shit with other bits before the 1{0}n
        #by shifting and calling recursion again we build it from top to bottom
