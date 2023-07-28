# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder, postorder):# List[int]) -> Optional[TreeNode]:
        preorder = collections.deque(preorder) # to not shift the whole list after poping
        return self.construct(preorder, postorder)

    def construct(self, pre, post):
        if post:
            if len(post) == 1:
                return TreeNode(pre.popleft())
            root_val = pre.popleft()
            ind = post.index(pre[0])
            root = TreeNode(root_val)
            root.left = self.construct(pre, post[:ind+1])
            root.right = self.construct(pre, post[ind+1:-1])
            return root

def main():
    sol = Solution()
    print(sol.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]))

if __name__ == "__main__": main()
