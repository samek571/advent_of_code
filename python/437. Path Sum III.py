# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        
        def dfs(node, sumage):
            if not node: return 0
            
            cunt = 0
            sumage+=node.val
            cunt = alles[sumage-target]

            alles[sumage]+=1
            cunt += dfs(node.left, sumage) + dfs(node.right, sumage)
            alles[sumage] -= 1

            return cunt

        alles = collections.defaultdict(int)
        alles[0]=1 # the case in which we dont have root and target is 0
        return dfs(root, 0)
