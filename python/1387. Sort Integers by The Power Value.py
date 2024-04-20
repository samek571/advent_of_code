from collections import defaultdict

class Solution:
    def picusko(self, num):

        if num == 1: return 0
        if num in self.memo: return self.memo[num]

        if num & 1:
            value = 1 + self.picusko(num * 3 +1)
        else:
            value = 1 + self.picusko(num >> 1)

        self.memo[num] = value
        return value


    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = defaultdict(int)

        return sorted(range(lo, hi+1), key=self.picusko)[k-1]


def main():
    sol = Solution()
    print(sol.getKth(12,15,2))
    print(sol.getKth(7,11,4))
    print(sol.getKth(1,1,1))

if __name__ == "__main__": main()

"""
7   16

8   3
9   19
10  6
11  14
12  9
13  9
14  17
15  17

16  4


"""


# class Solution:
#     def picusko(self, num):
#         plays = 0
#         while num > 1:
#             if num % 2 == 0:
#                 num /= 2
#             else:
#                 num = num * 3 + 1
#
#             plays += 1
#
#         return plays
#
#     def getKth(self, lo: int, hi: int, k: int) -> int:
#         array = []
#
#         for i in range(lo, hi+1):
#             array.append((i, self.picusko(i)))
#
#         array.sort(key=lambda x:x[1])
#         return array[k-1][0]


#class Solution:
#     def picusko(self, num):
#
#         if num == 1: return 0
#         if num in self.memo: return self.memo[num]
#
#         if num & 1:
#             value = 1 + self.picusko(num * 3 +1)
#         else:
#             value = 1 + self.picusko(num >> 1)
#
#         self.memo[num] = value
#         return value
#
#
#     def getKth(self, lo: int, hi: int, k: int) -> int:
#         self.memo = defaultdict(int)
#
#         return sorted(range(lo, hi+1), key=self.picusko)[k-1]