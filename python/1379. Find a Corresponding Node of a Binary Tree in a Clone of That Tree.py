# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):

        def binary(root):
            if not root: return
            if root.val == target.val: return root

            left = binary(root.left)
            right = binary(root.right)

            if left: return left
            if right: return right


        return binary(cloned)