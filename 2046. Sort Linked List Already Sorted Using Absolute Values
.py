# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''O(n) could be done as we iterate there is already being made the linked list and then we just connect them by one node which is O(1)'''
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=head
        while temp:
            if temp.val<0 and temp!=head:
                prev.next=temp.next
                temp.next=head
                head=temp
                temp=prev
            prev=temp
            temp=temp.next
        return head
