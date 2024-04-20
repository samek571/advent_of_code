# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        best = float("-inf")
        
        def get_max_gain(node):
            nonlocal best
            if node is None:
                return 0

            l = max(get_max_gain(node.left), 0)
            r = max(get_max_gain(node.right), 0)

            current_best = node.val + l + r
            best = max(best, current_best)

            return node.val + max(l, r)

        get_max_gain(root)
        return best
