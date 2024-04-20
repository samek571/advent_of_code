class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1 or (s[0]==")" and locked[0]=="1") or (s[-1]=="(" and locked[-1]=="1"):
            return False

        balance = 0
        for i in range(len(s)):
            balance += -1 if s[i] == ')' and locked[i] == '1' else 1
            if balance < 0:
                return False

        balance = 0
        for i in range(len(s) - 1, -1, -1):
            balance += -1 if s[i] == '(' and locked[i] == '1' else 1
            if balance < 0:
                return False

        return True

def main():
    sol = Solution()
    print(sol.canBeValid(s = "))()))", locked = "010100"))
    print(sol.canBeValid("()()", locked = "0000"))
    print(sol.canBeValid( s = ")", locked = "0"))

if __name__ == "__main__": main()

