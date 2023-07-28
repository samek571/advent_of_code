import collections

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:

        stck = [] ; popped = collections.deque(popped)

        for num in pushed:
            stck.append(num)

            while stck and popped and popped[0] == stck[-1]:
                stck.pop()
                popped.popleft()


        return not stck


def main():
    sol = Solution()
    print(sol.validateStackSequences([2,5,6,32,56] , [5,2,6,32,56] ))
    print(sol.validateStackSequences([1,2,3,4,5], popped = [4,5,3,2,1]))
    print(sol.validateStackSequences([1,2,3,4,5], popped = [4,3,5,1,2]))

if __name__ == "__main__": main()
