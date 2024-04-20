# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root) -> int:

        total = 0

        def dfs(node, zum):
            nonlocal total

            if not node.left and not node.right:
                total+=zum
                return

            if node.left:
                dfs(node.left, zum*10+node.left.val)

            if node.right:
                dfs(node.right, zum*10+node.right.val)

        dfs(root, root.val)
        return total

def main():
    sol = Solution()
    print(sol.sumNumbers([1,2,3]))
    print(sol.sumNumbers([4,9,0,5,1]))

if __name__ == "__main__": main()