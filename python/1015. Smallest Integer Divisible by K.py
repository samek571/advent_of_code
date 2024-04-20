class Solution:
    def smallestRepunitDivByK(k: int) -> int:

        reminder=0
        for i in range(1, k+1):
            reminder = (reminder*10+1)%k
            if reminder == 0: return i

        return -1

    print(smallestRepunitDivByK(3))