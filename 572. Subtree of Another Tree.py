# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # if self.dfs(subRoot) in self.dfs(root): return True
        # else: return False

        return self.dfs(subRoot) in self.dfs(root)
        


    def dfs(self, root):
        return "^" + str(root.val) + "#" + self.dfs(root.left) + self.dfs(root.right) if root else "$"
        # if not root: return ''
        # return self.dfs(root.left) + str(root.val) + self.dfs(root.right)
