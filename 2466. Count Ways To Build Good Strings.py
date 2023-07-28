import collections

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1);
        mod = 10 ** 9 + 7
        dp[0] = 1

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]

            if i - one >= 0:
                dp[i] += dp[i - one]

        return sum(dp[low:high + 1]) % mod



def main():
    sol = Solution()
    print(sol.countGoodStrings(low = 3, high = 3, zero = 1, one = 1))
    print(sol.countGoodStrings(low = 2, high = 3, zero = 1, one = 2))

if __name__ == "__main__": main()


        #
        # cnt=0 ; queue = collections.deque([''])
        # while queue:
        #     num = queue.popleft()
        #
        #     if len(num) <= high:
        #         queue.append(num+'0'*zero)
        #         queue.append(num+'1'*one)
        #
        #     if low <= len(num) <= high:
        #         cnt+=1
        #
        # return cnt
