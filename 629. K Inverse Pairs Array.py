import math

class Solution :
    def  kInversePairs(self, n,  k) :
        maxx = (n * (n-1)//2)
        if k > maxx: return 0
        if k == 0 or k == maxx: return 1
        
        k = min(k, maxx - k)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        M = 1000000007

        i = 1
        while (i <= n) :
            j = 0
            while (j <= k and j <= int(i * (i - 1) / 2)) :
                if (i == 1 and j == 0) :
                    dp[i][j] = 1
                    break
                elif (j == 0) :
                    dp[i][j] = 1
                else :
                    val = (dp[i - 1][j] + M - (dp[i - 1][j - i] if (j - i) >= 0 else 0)) % M
                    dp[i][j] = (dp[i][j - 1] + val) % M
                j += 1
            i += 1
        return dp[n][k]

def main():
    sol = Solution()
    print(sol.kInversePairs(6, 12)) #6, 3 --> 29
    print(sol.kInversePairs(3, 0))
    print(sol.kInversePairs(3, 1))
    print("###############")
    print(sol.kInversePairs(5, 5)) #5, 5 --> 22
    print(sol.kInversePairs(1,1))

if __name__ == "__main__": main()