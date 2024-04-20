# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root) -> bool:
        balanced = True
        
        def dfs(root):
            nonlocal balanced
            if not root: return -1

            height_left = dfs(root.left)
            height_right = dfs(root.right)

            if abs(height_left - height_right) > 1: balanced = False

            return 1 + max(height_left, height_right)
        
        dfs(root)
        return balanced

        '''
        0-0
        1-1
        2-2^2-1
        3-2^3-1
        4-2^4-1
        
        16 - 5
        15 - 4
        8 - 4
        7 -3
        4-3
        3-2
        2-2
        1-1
        '''

'''FOR SOME FUCKING REAASON IT DOESNT 0WIDJGFUIWNEFJ9UIGFhwejg98qewg nv879999 p9h77777777777777777777 dqwnt79fewI8N 3R2'''
        # if not root: return True
        #
        # maximum, count = 1, 0
        # def dfs(node, h):
        #     if not node: return
        #
        #     nonlocal maximum
        #     maximum = max(maximum, h)
        #
        #     dfs(node.left, h+1)
        #     dfs(node.right, h+1)
        #     nonlocal count
        #     count+=1
        #
        # dfs(root, maximum)
        # #print(maximum, count)
        # #math.floor(math.log(count, 2))+1
        #
        # if 2*math.log(count, 2)+2 > maximum: return False
        # return True