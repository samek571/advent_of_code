# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, acquired_depth):
            if not node: return acquired_depth
            
            elif not node.right:
                return dfs(node.left, acquired_depth+1)
            elif not node.left:
                return dfs(node.right, acquired_depth+1)
            
            return min(dfs(node.right, acquired_depth+1), dfs(node.left, acquired_depth+1))

        
        return dfs(root, 0)
