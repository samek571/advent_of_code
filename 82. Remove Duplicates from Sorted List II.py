# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen, banned = set(), set()

        #phase 1
        current = head
        while current:
            if current.val in seen: banned.add(current.val)
            seen.add(current.val)
            current = current.next

        dummy = ListNode(-1, head)
        prev = dummy
        current = head
        
        #phase 2 
        while current:
            if current.val in banned: prev.next = current.next
            else: prev = current

            current = current.next

        return dummy.next
