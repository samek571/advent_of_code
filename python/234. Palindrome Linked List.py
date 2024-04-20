# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import deque


class Solution:
    def isPalindrome(self, head) -> bool:
        '''
        for O(n) + O(1)
        with slow and fast pointer we can go to the middle and reverse the second half ofthe linked
        then iterate via both at the same time and check if they really are palindrome !(handle odd/even)
        '''
        '''to just get rid of it we iterate via ls and append each val to double ended queue - dequeue
        and then just pop simultaniously'''


        q, curNode = deque([]), head
        while curNode:
            q.append(curNode.val)
            curNode = curNode.next

        while len(q)>=2:

            a,b = q.popleft(), q.pop()
            if a!=b: return False

        return True
