# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, r, l):
            if not node: return True
            if not (l < node.val < r): return False


            return dfs(node.left, node.val, l) and \
                dfs(node.right, r, node.val)



        return dfs(root, float("inf"), -1*float("inf"))
