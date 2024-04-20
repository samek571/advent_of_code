class Solution:
    def longestValidParentheses(s: str) -> int:
        if len(s)<2:
            return 0

        left=right=output=counter=0

        for i in s:
            if i==")":
                right+=1
                if right>left:
                    left = right = 0
            elif i=="(":
                left+=1

            if left==right:
                counter=left*2
                if output<counter:
                    output=counter

        s=s[::-1]
        left = right =  counter = 0

        for i in s:
            if i==")":
                right+=1
            elif i=="(":
                left+=1
                if left>right:
                    left=right=0

            if left==right:
                counter=left*2
                if output<counter:
                    output=counter

        return output


    print(longestValidParentheses("()((())"))  # 4
    print(longestValidParentheses("))()(())(()()"))  # 6
    print(longestValidParentheses("()(()"))  # 2
    print(longestValidParentheses("))))()(()(("))  # 2
    print(longestValidParentheses("(()()))()"))  # 6
    print(longestValidParentheses(")()())()()()"))  # 6
    print(longestValidParentheses("(()))"))  # 4
    print("testcases:")
    print(longestValidParentheses("(()"))  # 2
    print(longestValidParentheses(")()())"))  # 4
    print(longestValidParentheses(""))  # 0
    print("aiojfhby8ufyas8fg")
    print(longestValidParentheses("((((()"))  # 2
    print(longestValidParentheses("((((()))"))  # 6
    print(longestValidParentheses("((((()))()"))  # 8