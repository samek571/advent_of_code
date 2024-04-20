# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key: int):# -> Optional[TreeNode]:
        if not root: return

        if root.val == key:
            if not root.left: return root.right
            if not root.right: return root.left

            # find leaf
            left_max = root.left
            while left_max.right:
                left_max = left_max.right

            # connect the leaf to popped element
            left_max.right = root.right
            return root.left


        elif root.val > key: root.left= self.deleteNode(root.left, key)
        elif root.val < key: root.right= self.deleteNode(root.right, key)

        return root
