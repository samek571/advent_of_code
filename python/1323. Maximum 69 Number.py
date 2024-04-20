class Solution:
    def maximum69Number(self, num: int) -> int:

        return int(str(num).replace('6', '9', 1))
def main():
    sol = Solution()
    print(sol.maximum69Number(996699))
    print(sol.maximum69Number(996999))
    print(sol.maximum69Number(696999))

if __name__ == "__main__": main()
