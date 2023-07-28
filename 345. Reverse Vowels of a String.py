class Solution:
    def reverseVowels(self, s: str) -> str:
        stck = []

        hovno = {"a", "e", "i", "o", "u", "A", "U", "E", "I", "O"}
        for i in s:
            if i in hovno: stck.append(i)

        new = ''
        for i in s:
            if i not in hovno:
                new+=i

            else:
                new += stck.pop()

        return new

def main():
    sol = Solution()
    print(sol.reverseVowels("hovna"))
    print(sol.reverseVowels("leetcode"))

if __name__ == "__main__": main()