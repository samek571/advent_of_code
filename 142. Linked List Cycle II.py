# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # either this or slow and fast pointer...
        
        if not locals(): return
        if (not head): return

        node, nodes = head, {head}
        while node.next:
            if node.next in nodes:
                return node.next
            nodes.add(node.next)
            node = node.next 
