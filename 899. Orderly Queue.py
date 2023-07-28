class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))

        # because at 2 we can do bubble sort
        else: return "".join(sorted(s))


def main():
    sol = Solution()
    print(sol.orderlyQueue("iufnbiundf", 2))
    print(sol.orderlyQueue("iufnbiundf", 3))
    print(sol.orderlyQueue("iufnbiundf", 1))

if __name__ == "__main__": main()



