class Solution:
    def isPerfectSquare(num: int) -> bool:
        if num==1: return True

        for i in range(num):

            if i*i>num: return False
            elif i*i == num: return True

        return False

    print(isPerfectSquare(1))
    print(isPerfectSquare(4))
    print(isPerfectSquare(9))
    print(isPerfectSquare(2))