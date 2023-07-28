import math
class Solution:
    def countPrimes(n: int) -> int:
        if n<3: #2
            return 0
        elif n<4:   #3
            return 1
        elif n<6:   #5
            return 2
        elif n<8:   #7
            return 3
        elif n<12:  #11
            return 4

        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):

            # If prime[p] is not changed, then it is a prime
            if (prime[p] == True):

                # Update all multiples of p
                for i in range(p ** 2, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False

        counter=0
        for p in range(n):
            if prime[p]:
                counter+=1

        return counter

        # #funkcne po 121 (throws bad values at 143)
        # secki=[2,3,5,7]
        # for i in range(11, n, 2):
        #     if i%3==0 or i%5==0 or i%7==0:
        #         continue
        #     else:
        #         secki.append(i)
        #
        # return (len(secki))

        # counter=1
        # for i in range(3, n, 2):
        #     washere=0
        #     for prime in range(3, int(math.floor(math.sqrt(i)))+1, 2):
        #         if i%prime==0:
        #             washere=1
        #             break
        #
        #     if washere==0:
        #         counter+=1
        #     continue
        #
        # return counter



    print(countPrimes(73))  #20
    print(countPrimes(234)) #51
    print(countPrimes(419)) #80
    print(countPrimes(420)) #81
    print(countPrimes(421)) #81
    print("testcases")
    print(countPrimes(10))
    print(countPrimes(0))
    print(countPrimes(1))
    print("asdasdasd")
    print(countPrimes(2))   #0
    print(countPrimes(4))   #2
    #print(countPrimes(54633))
    #print(countPrimes(5 * 10**6))
