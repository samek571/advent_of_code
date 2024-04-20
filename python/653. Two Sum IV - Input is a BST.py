class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def dfs(root, hashtable):
            if not root: return False
            
            if k-root.val in hashtable: return True
            hashtable.add(root.val)
            
            return dfs(root.left, hashtable) or dfs(root.right, hashtable)
        
        return dfs(root, set())
