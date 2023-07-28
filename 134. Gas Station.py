import  itertools


class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        '''we can simply say if the rout is doable based on the total cost being more than total gas
        then it doesnt matter where we start, since one of the gas stations
        (its gonna be just one since its unique solution promised) is the minimum of list meaning at
        that point we were in biggest debt therefore we have to start there to avoid going sub 0'''

        res = list(itertools.accumulate([r-c for r,c in zip(gas, cost)], initial=0))

        return -1 if res[-1]<0 else res.index(min(res))


def main():
    sol = Solution()
    print(sol.canCompleteCircuit([1,2,3,4,5], cost = [3,4,5,1,2]))
    print(sol.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))

if __name__ == "__main__": main()
