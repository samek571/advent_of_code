# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self) -> None:
        self.arr = []

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        #inorder dfs
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
        
        
        dfs(root)
        p_ix = self.arr.index(p.val)
        return TreeNode(self.arr[p_ix + 1]) if self.arr[-1] != self.arr[p_ix] else None
