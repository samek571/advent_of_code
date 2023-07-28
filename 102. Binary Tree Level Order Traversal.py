import collections
from collections import deque


class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, root):
        matrix = []
        if not root: return matrix

        lvl = 0
        dq = collections.deque([(root, lvl)])

        while dq:
            node, lvl = dq.popleft()

            if node:

                #securing the same amount of elements
                if len(matrix) == lvl:
                    matrix.append([])

                matrix[lvl].append(node.val)
                dq.append((node.left, lvl+1))
                dq.append((node.right, lvl+1))

        return matrix




