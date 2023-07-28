class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        n = len(num)


        hashmap = {"6":"9", "0":"0", "9":"6", "8":"8", "1":"1"}

        for i in range(n):
            if num[i] not in hashmap or hashmap[num[i]] != num[n-i-1]: return False

        return True



def main():
    sol = Solution()
    print(sol.isStrobogrammatic("1"))
    print(sol.isStrobogrammatic("2"))
    print(sol.isStrobogrammatic("320"))
    print(sol.isStrobogrammatic("69069"))
    print(sol.isStrobogrammatic("69096"))
    print(sol.isStrobogrammatic("962"))
    print(sol.isStrobogrammatic("88"))

if __name__ == "__main__": main()