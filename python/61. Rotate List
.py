# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        without array cheat there would be one iteration to get lenght, use % to get new k
        then make another empty linked list and by using slow fast with difference k adding there
        the nodes. return connected linked lists
        '''
        if not head: return

        curr, arr = head, []
        while curr:
            arr.append(curr.val)
            curr = curr.next

        l = len(arr)
        k = k%l
        if k==0: return head

        arr = arr[l-k:] + arr[:l-k]
        
        cur = dummy = ListNode(0)
        for e in arr:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next


