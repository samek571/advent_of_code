import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root):#> List[List[int]]:

        o=[ [] for i in range(2000) ] ; q = collections.deque([[root, 0]])

        while q:
            node, lvl = q.popleft()
            if node:
                o[lvl].append(node.val)

                if node.left: q.append([node.left, lvl+1])
                if node.right: q.append([node.right, lvl+1])

        return [i for i in o if len(i)>0][::-1]

def main():
    sol = Solution()
    print(sol.levelOrderBottom(TreeNode(1)))
    print(sol.levelOrderBottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

if __name__ == "__main__": main()