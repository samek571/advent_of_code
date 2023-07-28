# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:

        def dfs(node, cum):

            if not node:
                return False

            cum+=node.val

            if not node.right and not node.left:
                if cum == targetSum:
                    return True
                return False

            return dfs(node.left, cum) or dfs(node.right, cum)

        return dfs(root, 0)