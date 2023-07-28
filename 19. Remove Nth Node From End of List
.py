# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''one iter to get lenght of ls, subtract n from l and perform deletion in another binary deremination pass - for simplicity i will just iterate since the maxlenght is 30'''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        l=0
        while curr:
            l+=1
            curr = curr.next

        prev=l-n-1
        if prev == -1: return head.next

        slow = head
        for _ in range(prev):
            slow = slow.next
        
        slow.next = slow.next.next
        return head
