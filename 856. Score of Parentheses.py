class Solution:
    def scoreOfParentheses(s: str) -> int:
        stacc=[0]

        for i in s:
            if i == ")":
                last=stacc.pop()
                stacc[-1] += max(2*last, 1)

            else: stacc.append(0)
        return stacc[-1]

    print(scoreOfParentheses("((()()()))"))
    print(scoreOfParentheses("(()())"))
    print(scoreOfParentheses("(((())))"))
