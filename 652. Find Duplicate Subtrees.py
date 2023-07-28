# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''dfs in which we store path, each path is added to the hashmap
    final iteration over hashmap and taking path if has more than 2 encounters'''

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(int)
        dup = []

        def find(root):
            if root is None:
                return "#"  # at leaf node, add # to key

            l = find(root.left)
            r = find(root.right)

            k = str(root.val) + "." + l + "." + r + "."  # essential to add special char to distinguish value
            # e.g. 1, 11 or 11, 1
            seen[k] += 1

            if seen[k] == 2:
                dup.append(root)

            return k  # return key to save to seen

        find(root)
        return dup