# Definition for singly-linked list.

'''
you are given a linked list in python,
- iterate it to get its lenght 
- from the 0th index run slow and fast by difference of lenght-k (in which k is given)
- swap kth and lenght-k th node
'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        

        # calculate positions of nodes to swap
        pos1 = k-1
        pos2 = length-k
        
        if length == 1 or pos2==pos1: return head
        
        
        # iterate to node positions
        curr = head
        prev1 = None
        prev2 = None
        for i in range(length):
            if i == pos1:
                node1 = curr
            elif i == pos2:
                node2 = curr
            if i == pos1-1:
                prev1 = curr
            elif i == pos2-1:
                prev2 = curr
            curr = curr.next
        
        

        # swap nodes
        if node1 != node2:
            if prev1:
                prev1.next = node2
            else:
                head = node2
            if prev2:
                prev2.next = node1
            else:
                head = node1
            temp = node1.next
            node1.next = node2.next
            node2.next = temp
        
        return head
