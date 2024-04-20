class Solution:
    '''
    a more interesting variation would be to return one number - the number of 1s in range from 0 to number
    I think people would not do in optimal O(lgn) as using the rule in each full 2^(n-1) there is amount of 1 equal to amount of 0 -> therefore it would be doing easy math
    '''

    #dp
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
