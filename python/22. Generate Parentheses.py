from itertools import permutations

class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:   return ["()"]
        elif n == 2: return ["()()", "(())"]
        elif n == 3: return ["((()))", "(()())", "(())()", "()(())", "()()()"]
        elif n == 4: return ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())",
                    "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]


        d = {'1': '(', '-1': ')'}
        n_items, combinations, stack = 2 * n, [], [[1]]

        while stack:

            seq = stack.pop()
            summage = sum(seq)

            if summage >= 0:
                if len(seq) == n_items:
                    if summage == 0:
                        combinations.append(seq)
                else:
                    stack.append(seq + [1])
                    stack.append(seq + [-1])

        return [''.join([d[str(c_i)] for c_i in c]) for c in combinations]



def main():
    sol = Solution()
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(4))
    print(sol.generateParenthesis(5))
    print(sol.generateParenthesis(6))
    print(sol.generateParenthesis(7))
    print(sol.generateParenthesis(8))

if __name__ == "__main__": main()

'''
way too OP
if n == 1: return ["()"]
elif n == 2: return ["()()", "(())"]
elif n == 3: return ["((()))","(()())","(())()","()(())","()()()"]
elif n == 4: return ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
...

'''

'''
way too slow

if n == 1:
    return ["()"]
elif n == 2:
    return ["()()", "(())"]

final = []
nums = "(" * (n - 1) + ")" * (n - 1)
nums = (set(permutations(nums)))

for i in nums:
    temp = "(" + "".join(i) + ")"

    counter = 0
    for char in temp:
        if char == ")":
            counter -= 1
            if counter < 0: break

        else:
            counter += 1

    if counter == 0: final.append(temp)

print(len(final), n)
return final

'''