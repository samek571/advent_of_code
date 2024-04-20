# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
postorder dfs

'''
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def postorder_dfs(node):
            if node is None:
                return (0, 0)  # Return (sum, count) tuple for empty subtree
            
            left_sum, left_count = postorder_dfs(node.left)
            right_sum, right_count = postorder_dfs(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            avg = total_sum / total_count
            if math.floor(avg) == node.val:
                nonlocal cnt
                cnt+=1


            return (total_sum, total_count)  # Return (sum, count) tuple for valid subtree
        
        cnt=0
        postorder_dfs(root)
        return cnt

# class Solution:
#     def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
#         def postorder_dfs(node, cnt):
#             if node is None:
#                 return (0, 0, cnt)  # Return (sum, count, cnt) tuple for empty subtree
            
#             left_sum, left_count, cnt = postorder_dfs(node.left, cnt)
#             right_sum, right_count, cnt = postorder_dfs(node.right, cnt)
            
#             total_sum = left_sum + right_sum + node.val
#             total_count = left_count + right_count + 1
            
#             avg = total_sum / total_count
#             if math.floor(avg) == node.val:
#                 cnt += 1  # Increment the cnt variable

#             return (total_sum, total_count, cnt)  # Return (sum, count, cnt) tuple for valid subtree
        
#         _, _, cnt = postorder_dfs(root, 0)  # Call the postorder_dfs function with cnt as 0
#         return cnt
