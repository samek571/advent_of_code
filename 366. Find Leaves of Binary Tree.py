# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root):# -> List[List[int]]:
        output=[]

        def dfs(node):
            if not node: return None

            if not(node.left or node.right):
                output[-1].append(node.val)
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

        while root:
            output.append([])
            root = dfs(root)

        return output

def main():
    sol = Solution()
    print(sol.findLeaves())

if __name__ == "__main__": main()


