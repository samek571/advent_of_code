class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()

        if len(s_list) != len(pattern): return False


        a , b = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in a:
                if a[pattern[i]] != s_list[i]: return False
            else:
                a[pattern[i]] = s_list[i]

            if s_list[i] in b:
                if b[s_list[i]] != pattern[i]: return False
            else:
                b[s_list[i]] = pattern[i]

        return True


def main():
    sol = Solution()
    print(sol.wordPattern("abba", s = "dog cat cat"))
    print(sol.wordPattern("abba", s = "dog cat cat dog"))

if __name__ == "__main__": main()