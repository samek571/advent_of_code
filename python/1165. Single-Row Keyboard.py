class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        output, dck = 0, dict()

        cnt=0
        for i in keyboard:
            dck[i]=cnt
            cnt+=1

        last = 0
        for idx in range(len(word)):
            output+=abs(dck[word[idx]] - last)
            last = dck[word[idx]]

        return output




def main():
    sol = Solution()
    print(sol.calculateTime(keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"))
    print(sol.calculateTime(keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"))

if __name__ == "__main__": main()