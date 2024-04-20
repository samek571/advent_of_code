import copy


class Solution:
    def grayCode(self, n: int) -> list[int]:

        res = [0, 1]
        k = 1 #k-th iteration

        # append the reverse incremented by 2**(k-1)
        # [0,1] + [1+2,0+2] = [0,1,3,2]
        # [0,1,3,2] + [2+4, 3+4, 1+4, 0+4] = [0,1,3,2,6,7,5,4]
        # ...
        while k < n:
            k += 1

            temp = copy.deepcopy(res)
            increment = 2 ** (k - 1)
            for i in range(len(temp) - 1, -1, -1):
                res.append(temp[i] + increment)

        return res
