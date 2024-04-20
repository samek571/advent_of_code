class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        #mega gay case
        if len(needle) == 0: return 0
        elif haystack.find(needle) == -1: return -1
        else: return haystack.index(needle)

        #case in which you get 0<needle and haystick
        #return haystack.find(needle)

def main():
    sol = Solution()
    print(sol.strStr(haystack = "hello", needle = "ll"))
    print(sol.strStr( "aaaaa", needle = "bba"))
    #print(sol.strStr( "aaaaa", needle = ""))

if __name__ == "__main__": main()
