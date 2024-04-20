# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):# -> Optional[ListNode]:

        s1, s2 = '', ''

        while l1 and l2:
            s1+= str(l1.val)
            s2+= str(l2.val)
            l1 = l1.next
            l2 = l2.next

        while l1:
            s1+= str(l1.val)
            l1 = l1.next

        while l2:
            s2+= str(l2.val)
            l2 = l2.next

        s = str(int(s1[::-1]) + int(s2[::-1]))

        curr = dummy = ListNode(0)
        for i in range(len(s)-1,-1,-1):
            curr.next = ListNode(s[i])
            curr = curr.next

        return dummy.next