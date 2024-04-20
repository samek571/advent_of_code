# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        if not first: return second
        elif not second: return first

        #2 pointers
        cur = dummy = ListNode()
        while second and first:
            
            # choosing the lower val to join the dummy
            if first.val >= second.val:
                cur.next = second
                second, cur = second.next, second
            else:
                cur.next = first
                first, cur = first.next, first

        #fill
        if first: cur.next = first
        elif second: cur.next = second


        return dummy.next
