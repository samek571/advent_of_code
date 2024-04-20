#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # onespass implementation would be to go further by r-l, then get both pointers at start/end accordingly.
    # prev of left points at next of right and the left basically reverse linked list on the segment
    # need to choose sufficient amount of pointers 

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        #delta of pointers        
        for i in range(left - 1):
            prev = prev.next
        
        #relink innit
        start = prev.next
        end = start.next
        
        # Reverse
        for i in range(right - left):
            
            start.next = end.next
            end.next = prev.next
            prev.next = end
            end = start.next
        
        return dummy.next

