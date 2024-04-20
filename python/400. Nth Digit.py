class Solution:
    def findNthDigit(n: int) -> int:
        digit = base = 1 # starting from 1 digit
        while n > 9*base*digit: # upper limit of d digits
            n -= 9*base*digit
            digit += 1
            base *= 10
        q, r = divmod(n-1, digit)
        return int(str(base + q)[r])


    print(findNthDigit(2**12-1))
    print(findNthDigit(20))
    print(findNthDigit(12))
    print(findNthDigit(13))
    print(findNthDigit(14))
    print(findNthDigit(2**31-1))
    print(findNthDigit(15))
    print(findNthDigit(16))
    print(findNthDigit(17))
    print(findNthDigit(18))
    print(findNthDigit(19))
    print(findNthDigit(190))
    print(findNthDigit(191))
    print(findNthDigit(1950))
    print(findNthDigit(189))

        # #pomale hovno
        # if n < 10: return n
        #
        # future_counter=[9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889]
        # future_i=[9,99,999,9999,99999,999999,9999999,99999999, 999999999]
        #
        # i=10
        # counter=9
        #
        # for hovno in range(len(future_i)):
        #     if future_counter[hovno]>=n:
        #         i = future_i[hovno-1]
        #         counter = future_counter[hovno-1]
        #         break
        #
        #
        # while True:
        #     for smth in str(i):
        #         counter+=1
        #         if counter==n: return smth
        #
        #     i+=1


        # edges=[9]
        # number="9"
        # sucet=9
        # while sucet<n:
        #     number+="0"
        #     dlzka=len(number)
        #     sucet+=int(number)*dlzka
        #     edges.append(sucet)
        #
        # if n in edges: return 9
        # print(edges)
