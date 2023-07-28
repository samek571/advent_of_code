# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x: int) -> Optional[ListNode]:

        less = collections.deque([])
        more = collections.deque([])

        curr = head
        while curr:
            if x>curr.val: less.append(curr.val)
            else: more.append(curr.val)
            curr = curr.next
        

        cur = dummy = ListNode(0)
        for e in less:
            cur.next = ListNode(e)
            cur = cur.next
        
        for e in more:
            cur.next = ListNode(e)
            cur = cur.next
        

        return dummy.next
