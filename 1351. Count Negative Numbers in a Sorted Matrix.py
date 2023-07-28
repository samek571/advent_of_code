class Solution:
    def negativeCounter(self, lst) -> int:
        l = 0
        r = len(lst) - 1
        count = 0

        while l <= r:
            mid = l + (r - l) // 2
            if lst[mid] >= 0:
                l = mid + 1
            else:
                count += r - mid + 1
                r = mid - 1
        return count

    def countNegatives(self, grid) -> int:

        count = 0
        for item in grid:
            count += self.negativeCounter(item)
        return count

def main():
    sol = Solution()
    print(sol.countNegatives())

if __name__ == "__main__": main()