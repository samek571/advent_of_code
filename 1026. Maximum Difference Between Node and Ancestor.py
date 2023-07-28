# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root) -> int:
        if not root: return 0
        self.output = 0

        def dfs(node, cur_max, cur_min):
            if not node: return
            
            self.output = max(self.output, abs(cur_max-node.val), abs(cur_min-node.val))

            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            dfs(node.left, cur_max, cur_min)
            dfs(node.right, cur_max, cur_min)

        dfs(root, root.val, root.val)
        return self.output