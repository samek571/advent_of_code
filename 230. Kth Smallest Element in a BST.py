# Definition for a binary tree node.
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        #preorder
        def dfs(root):
            nonlocal arr
            if not root: return

            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)
            return root

        arr = []
        dfs(root)
        arr.sort()
        return arr[k-1]


def main():
    sol = Solution()
    print(sol.kthSmallest([3,1,4,None,2], k = 1))
    print(sol.kthSmallest([5,3,6,2,4,None,None,1], k = 3))

if __name__ == "__main__": main()


'''
        #preorder
        def dfs(root):
            nonlocal arr
            if not root: return

            heapq.heappush(arr, root.val)
            dfs(root.left)
            dfs(root.right)
            return root

        k-=1
        arr = []
        heapq.heapify(arr)
        dfs(root)
        return heapq.nsmallest(k, arr)

'''