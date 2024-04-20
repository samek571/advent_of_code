''' 
first thing is to actually google up something
interesting to know is there is a database of many sequences
https://oeis.org/search?q=1%2C0%2C0%2C2%2C10%2C4%2C40%2C92%2C352&language=english&go=Search
right second reference is a rewritten problem
'''
class Solution:
    def totalNQueens(self, n: int) -> int:

        def check_permutation(p):
            for i, j in itertools.permutations(range(len(p)), 2):
                if abs(p[j] - p[i]) == abs(j - i):
                    return False
            return True


        perms = itertools.permutations(range(1, n+1))
        valid_perms = 0
        for p in perms:
            if check_permutation(p):
                valid_perms+=1

        return valid_perms
