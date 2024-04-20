# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root):# Optional[TreeNode]) -> List[List[int]]:
        # massive = collections.defaultdict(list)
        # q=collections.deque([(root,0, 0)])
        #
        # while q:
        #     node, order, pos = q.popleft()
        #     if node:
        #         massive[pos].append((order, node.val))
        #
        #         q.append((node.right, order+1, pos+1))
        #         q.append((node.left, order+1, pos-1))
        #
        #
        # vals = dict(sorted(massive.items()))
        # res = []
        # # Loop through our sorted dict appending vals sorted by height (top down order).
        # for k, v in vals.items():
        #     res.append([x[1] for x in sorted(v, key=lambda x: x[0])])
        #
        # return res
        cols = collections.defaultdict(list)
        q = [(root, 0)]
        for node, i in q:
            if node:
                cols[i].append(node.val)
                q += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]



def main():
    sol = Solution()
    print(sol.verticalOrder(TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))))
    print(sol.verticalOrder(TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, TreeNode(5), TreeNode(2))), TreeNode(8, TreeNode(1), TreeNode(7)))))

if __name__ == "__main__": main()