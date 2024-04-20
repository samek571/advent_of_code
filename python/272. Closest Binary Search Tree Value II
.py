# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        '''find all values and sort them - could be done in heapq but fuck that'''
        l = []
        def dfs(node):
            if node:
                l.append(node.val)
                dfs(node.left)
                dfs(node.right)

            return
        dfs(root)
        l.sort()


        ret = []
        '''binary find closest and 2 pointers outwards'''
        if len(l) == k:
            return l

        index = bisect.bisect_left(l, target)
        left = index - 1
        right = index

        while k > 0:
            #2edge cases in case one pointer is at its end
            if left < 0:
                ret.append(l[right])
                right += 1
            elif right >= len(l):
                ret.append(l[left])
                left -= 1

            #usually this gets executed
            elif abs(target - l[left]) < abs(target - l[right]):
                ret.append(l[left])
                left -= 1
            else:
                ret.append(l[right])
                right += 1

            k -= 1

        return ret
