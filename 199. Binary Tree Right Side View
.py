# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def dfs(node, d):
            if not node: return 

            elif len(result) <= d:
                result.append(node.val)

            dfs(node.right, d+1)
            dfs(node.left, d+1)
            return


        result = []
        dfs(root, 0)
        return result


