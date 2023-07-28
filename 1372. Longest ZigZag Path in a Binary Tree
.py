# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2 consecutive right turns make it 1
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        q = collections.deque([[root, True, 0]]) ; res = 0
        while q:
            node, prevLeft, lvl = q.popleft()
            res = max(lvl, res)
            
            if node.left:
                if prevLeft: q.append([node.left, True, 1])
                else: q.append([node.left, True, lvl+1])

            if node.right:
                if prevLeft: q.append([node.right, False, lvl+1])
                else: q.append([node.right, False, 1])

        return res
