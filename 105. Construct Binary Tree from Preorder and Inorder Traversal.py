# Definition for a binary tree node.
from collections import deque as deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):# List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder) # to not shift the whole list after poping
        return self.getTree(preorder,inorder)
    
    # making another fx cuz leetcode runs the buildTree
    def getTree(self,preorder,inorder):
        # if there is a problem to take care of
        if inorder:

            # preorder visits first and inorder after exiting from the first visit ==> 
            # first element preorder is always the root of the sub tree therefore we can keep spliting the
            # cases by the roots (which actually even add up to the tree we want so its more useful even)
            # if we get the case like there is no 2 sub problems to be seen, we have fount the leaf 
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])
            root.left = self.getTree(preorder,inorder[:idx])
            root.right = self.getTree(preorder,inorder[idx+1:])
            return root
