# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):# -> Optional[ListNode]:

        #traversing the whole ls
        curr = head
        while curr and curr.next:

            # if we encounter 2 identical values, we run a cycle checking if it is more than 2
            while curr.next and curr.val == curr.val.next:
                curr.next = curr.next.next

            # moving the pointer nevertheless
            curr = curr.next

        return head