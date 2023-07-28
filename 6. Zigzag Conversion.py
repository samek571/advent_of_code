class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s

        output, lenght, k = '', len(s), 2*numRows-2
        for i in range(numRows):

            if i in {0, numRows-1}:
                for j in range(0, lenght, k):
                    if j+i < lenght:
                        output += s[j+i]

            else:
                for j in range(0, lenght, k):
                    if j + i < lenght: output+=s[i+j]
                    if j+k-i < lenght: output+=s[j+k-i]


        return output


def main():
    sol = Solution()
    print(sol.convert('abcdefghijklmnopqrstuvwxyz', 5))
    print(sol.convert('abcdefghijklmnopqrstuvwxyz123', 5))
    print(sol.convert('abcdefghijklmnopqrstuvwxyz', 2))
    print(sol.convert('abcdefghijklmnopqrstuvwxyz', 1))
    print(sol.convert('abcdefghijklmnopqrstuvwxyz', 3))
    print(sol.convert('abcdefghijklmnopqrstuvwxyz', 4))
    print(sol.convert('abcdefghijklmnopqrstuvwxyz', 6))

if __name__ == "__main__": main()