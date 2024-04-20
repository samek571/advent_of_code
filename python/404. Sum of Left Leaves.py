# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        cum = 0

        def dfs(node, isleft):
            nonlocal cum

            if not node:
                return


            if not node.left and not node.right and isleft:
                cum += node.val


            dfs(node.left, True)
            dfs(node.right, False)


        dfs(root, False)
        return cum
