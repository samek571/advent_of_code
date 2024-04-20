# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        self.summendo = 0
        def dfs(root):
            if not root: return

            if root.val <= high and root.val >= low:
                self.summendo+=root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.summendo




