# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''O(nlogn) O(1) could be done with merge sort implementation inside of the linked list'''
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr.sort()


        cur = dummy = ListNode(0)
        for e in arr:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
