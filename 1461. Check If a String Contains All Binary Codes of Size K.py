class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k or not s: return False

        num = 0
        for i in range(k):
            num += (2 ** (k - i - 1)) * int(s[i])

        nums = set()
        nums.add(num)

        for j in range(k, n):
            num = ((num << 1) & (2 ** k - 1)) + int(s[j])
            nums.add(num)

        return len(nums) == (2 ** k)

def main():
    sol = Solution()
    print(sol.hasAllCodes())

if __name__ == "__main__": main()