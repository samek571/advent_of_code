#Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.arr = collections.deque(self.dfs(root))

    def dfs(self, root):
        if not root: return []
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)

    def next(self) -> int:
        return self.arr.popleft()

    def hasNext(self) -> bool:
        if self.arr: return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()