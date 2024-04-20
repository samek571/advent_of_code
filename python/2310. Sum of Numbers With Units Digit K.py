class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        ending=num%10

        if num == 0: return 0
        elif ending==k: return 1

        possibilities={}
        for i in range(1,11):
            if (k*i)%10 not in possibilities:
                possibilities[(k*i)%10]=i

        if ending not in possibilities: return -1

        minimal = possibilities[ending]
        if minimal*k>num: return -1
        else: return minimal



def main():
    sol = Solution()
    print(sol.minimumNumbers(58, 9))
    print(sol.minimumNumbers(17, 9))
    print(sol.minimumNumbers(37,2))
    print(sol.minimumNumbers(0, 7))
    print(sol.minimumNumbers(2235, 7))

if __name__ == "__main__": main()