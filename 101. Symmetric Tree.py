# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mirroraren(self, l, r):
        #base case
        if not l and not r: return True
        if not l or not r: return False

        #recursive case
        return l.val == r.val and self.mirroraren(l.right, r.left) and self.mirroraren(l.left, r.right)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirroraren(root, root)