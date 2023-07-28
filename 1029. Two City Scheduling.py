class Solution:
    '''mark left minus right, make priority sort, take lower half and upper one separately'''
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2 ; new = sorted([(left-right, left, right) for left, right in costs])
        return sum(x[1] for x in new[:n]) + sum(x[2] for x in new[n:])
