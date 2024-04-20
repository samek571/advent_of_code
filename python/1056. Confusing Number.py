class Solution:
    def confusingNumber(self, n: int) -> bool:
        banned = {'2','3','4','5','7'}
        conv = {'1':'1', '6':'9', '9':'6', '0':'0', '8':'8'}
        n = str(n)
        new = ''

        for i in range(len(n)-1,-1,-1):
            if n[i] in banned: return False
            else: new+=conv[n[i]]

        # new = new.lstrip('0')
        # return not new == n[::-1]

        return  not int(new) == int(n)


def main():
    sol = Solution()
    print(sol.confusingNumber(25))
    print(sol.confusingNumber(80))
    print(sol.confusingNumber(8))
    print(sol.confusingNumber(4))
    print(sol.confusingNumber(0))

if __name__ == "__main__": main()