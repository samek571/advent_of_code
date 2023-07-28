class Solution:
    '''sort and bs'''
    def hIndex(self, cit: List[int]) -> int:

        cit.sort()
        n = len(cit)
        count = 0
        for i in range(n - 1, -1, -1):
            if (n - i) <= cit[i]:
                count += 1
        return count
