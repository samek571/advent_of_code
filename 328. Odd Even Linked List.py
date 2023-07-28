        #set pointer to tail by iteration
        #make another O(n) iteration in which the slow pointer
        # - moves by 2
        # - removes each node it encounters & appends it at the end
        # - there is another (third) pointer that points the current tail
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
