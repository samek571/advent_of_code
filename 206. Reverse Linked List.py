# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

        if head:

            prev = None
            while head.next:
                head.next, head, prev = prev, head.next, head

            head.next = prev

        return head
