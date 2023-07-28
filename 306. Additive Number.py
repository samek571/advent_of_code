class Solution:
    def isAdditiveNumber(self, s: str) -> bool:

        n = len(s)
        for i in range(1, n):
            for j in range(i+1, n+1):
                a = s[:i] ; b = s[i:j] ; c=0

                if a != str(int(a)) or b != str(int(b)): continue

                while j < n:
                    c = str(int(a) + int(b))
                    if not s.startswith(c, j):
                        break
                    j += len(c)
                    a, b = b, c

                if n == j and c:
                    return True

        return False



def main():
    sol = Solution()
    print(sol.isAdditiveNumber("120122436"))
    print(sol.isAdditiveNumber("101"))

if __name__ == "__main__": main()