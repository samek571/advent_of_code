# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        1. find middle
        2. reverse second part of the list
        3. merge 2 lists
        """
        if not head: return

        #1
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #2
        prev, curr = None, slow
        while curr:
            curr.next, curr, prev = prev, curr.next, curr

        #3
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
