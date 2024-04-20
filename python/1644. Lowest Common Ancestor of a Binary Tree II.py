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

        # simple dfs traversal if we have p and q
        def dfs(root, p, q):
            nonlocal cnt
            if not root:
                return
            elif root == p or root == q:
                cnt += 1

            dfs(root.left, p, q)
            dfs(root.right, p, q)

        cnt = 0
        dfs(root, p, q)
        # if we have both we can run the actual reused 236. ltc problem
        # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
        if cnt == 2:
            return self.travel(root, p, q)
        else:
            return None

    def travel(self, root, p, q):
        if not root: return
        if root == q or root == p: return root

        l = self.travel(root.left, p, q)
        r = self.travel(root.right, p, q)

        if l and r: return root
        if not l and not r: return

        if l: return l
        return r







