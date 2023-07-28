class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1][0]: stack.append([char,1])

            elif stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k: stack.pop()


        return "".join(char * count for char, count in stack)



def main():
    sol = Solution()
    print(sol.removeDuplicates( s = "deeedbbcccbdaa", k = 3))

if __name__ == "__main__": main()