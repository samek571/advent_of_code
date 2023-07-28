# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def PathSum(self, root, targetSum: int) -> bool:

        output_arr=[]

        def dfs(node, arr, cum):

            if not node:
                return

            cum+=node.val

            if not node.right and not node.left and cum == targetSum:
                output_arr.append(arr+ [node.val])

            dfs(node.left, arr+ [node.val], cum)
            dfs(node.right, arr+ [node.val], cum)

        dfs(root, [], 0)
        return output_arr



        # output_arr=[]
        #
        # def dfs(node, arr, cum):
        #
        #     if not node:
        #         return
        #
        #     cum+=node.val
        #     arr += [node.val]
        #
        #     if not node.right and not node.left:
        #         if cum == targetSum:
        #             output_arr.append(arr)
        #
        #     dfs(node.left, arr, cum)
        #     dfs(node.right, arr, cum)
        #
        # dfs(root, [], 0)
        # return output_arr