from itertools import combinations

class Solution:
    def combine(n: int, k: int):
        array=[i for i in range(1, n+1)]
        array = list(combinations(array, k))

        for i in range(len(array)): array[i]= list(array[i])
        return array

    print(combine(4, 2))
    print(combine(1, 1))
    print(combine(19, 3))