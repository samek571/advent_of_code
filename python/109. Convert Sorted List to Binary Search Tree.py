#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''where in the fucking fuck they mentioned hbbst has to be sorted??
    We have 2 solutions as if now:
    1. the more intuitive but probably doesnt get accepted cuz its not sorted (btw it would be a good thing to define whats sort of a tree) -- build a tree on the go while doing bfs -- new depth cant be built if we havent finnished current -- thereofre always fucking balanced as it requires
    2. implementing merge sort -- slow&fast halving
    2.1. make arr from ls and do the merge sort ; but thats a time/space trade off
    '''

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head: return
        if not head.next: return TreeNode(head.val)

        slow , fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.right = self.sortedListToBST(tmp.next)
        root.left = self.sortedListToBST(head)
        return root
