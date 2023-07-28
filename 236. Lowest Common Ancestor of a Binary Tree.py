# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs first (any p / q) and pass it to the parent, which eventually passes it to the root
        # once any parent (or root) gets 2 numbers passed (not null if we dont find the p|q in the branch)
        # we have our result,
        # if p is parent of q it gets handled because root gets just one p passed

        if not root: return
        if root == q or root == p: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: return root
        if not l and not r: return

        if l: return l
        return r




def main():
    sol = Solution()
    print(sol.lowestCommonAncestor(root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1))
    print(sol.lowestCommonAncestor(root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4))

if __name__ == "__main__": main()
