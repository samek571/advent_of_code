# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root) -> int:

        if not root: return 0

        def findDepth(node):
            if not node.left:
                return 0
            return findDepth(node.left) + 1

        def check(node, mid, curDepth, left, right):
            if curDepth == depth: return True if node else False
            if mid <= (left + right) // 2:
                return check(node.left, mid, curDepth + 1, left, (left + right) // 2)
            else:
                return check(node.right, mid, curDepth + 1, (left + right) // 2, right)

        depth = findDepth(root)
        lastLevelLength = 2 ** depth

        s, e = 1, lastLevelLength + 1
        while s + 1 < e:
            mid = (s + e) // 2
            if check(root, mid, 0, 1, lastLevelLength):
                s = mid
            else:
                e = mid

        return lastLevelLength - 1 + s