# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = collections.deque([[root,0]]) ; res = 0
        while q:
            #handles the case in which there is only one at the last level AND
            #checks regurarly by levels if we have a new maximum -> good implementation of logic
            res = max(res, q[-1][1]-q[0][1]) 

            for _ in range(len(q)):
                node, n = q.popleft()

                if node.left: q.append([node.left, n*2-1])
                if node.right: q.append([node.right, n*2])
        
        return res+1
