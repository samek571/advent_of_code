class Solution:
    def judgeSquareSum(c) -> bool:
        if c<3:
            return True

        hashmap = dict()
        for i in range(c):
            if i * i > c:
                break

            hashmap[i * i] = 1

            if (c - i * i) in hashmap.keys():
                return True

        return False

    print(judgeSquareSum(1))    #t
    print(judgeSquareSum(2))    #t
    print(judgeSquareSum(3))    #f
    print(judgeSquareSum(4))    #t
    print(judgeSquareSum(5))    #t

    print(judgeSquareSum(14))
    print(judgeSquareSum(234))
