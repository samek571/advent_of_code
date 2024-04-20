# Definition for singly-linked list.
'''
the point is to traverse to the mid and rotate the linked list to achieve O(1) space c
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        curr = head ; arr=[] ; lenght = 0
        while curr:
            arr += [curr.val]
            curr = curr.next
            lenght+=1
        print(arr)

        i, j = 0, len(arr) - 1 ; res = 0
        while i < j:
            res = max(res, arr[i] + arr[j])
            i += 1 ; j -= 1
        
        
        return res
