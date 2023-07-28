# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if root:
                q.append(root)
                dfs(root.left)
                dfs(root.right)

        q = []
        dfs(root)

        #building
        for i in range(len(q) - 1):
            q[i].right = q[i + 1]
            q[i].left = None