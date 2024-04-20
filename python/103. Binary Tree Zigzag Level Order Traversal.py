# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):# -> List[List[int]]:
        if not root: return []


        q, o, l_to_right = collections.deque([root]), [], True
        while q:
            tmp, n = [], len(q)
            for _  in range(n):
                node = q.popleft()
                tmp.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if not l_to_right: tmp = tmp[::-1]
            o.append(tmp)

            l_to_right = not l_to_right

        return o


def main():

    new_tree = TreeNode([1,9,11,17])
    print(new_tree.__init__(new_tree.root))

if __name__ == "__main__": main()
