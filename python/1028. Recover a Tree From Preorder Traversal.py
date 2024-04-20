# Definition for a binary tree node.
import collections
import re


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #parse by regex and use simple dfs>bfs
    #uniquenes: If a node has only one child, that child is guaranteed to be the left child.
    def recoverFromPreorder(self, traversal: str):
        matches = re.findall('(-*)(\d+)',traversal)
        dq = collections.deque([(int(match[1]), len(match[0])) for match in matches])

        #preorder dfs
        def dfs(parent=None, depth=0, pos=''):
            #finished or it is necesarry to change depth
            if not dq or dq[0][1] < depth: return
            
            node = TreeNode(val=dq[0][0])
            dq.popleft() #popping just now because sooner might fuck things up
            if parent:
                if pos == 'left':
                    parent.left = node
                else:
                    parent.right = node

            #preorder
            dfs(node, depth+1, 'left')
            dfs(node, depth+1, 'right')

            return node


        root = dfs()
        return root


def main():
    sol = Solution()
    print(sol.recoverFromPreorder("1-2--3--4-5--6--7"))

if __name__ == "__main__": main()