# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head):# ListNode) -> ListNode:
        '''
        each new value gets added to the set named "seen", if seen already contains the value - it gets added to second set which stores banned values
        in 2nd iteration of the ls we just ignore all vals that are in banned
        '''
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





def main():
    sol = Solution()
    print(sol.deleteDuplicatesUnsorted(head = [1,2,3,2]))
    print(sol.deleteDuplicatesUnsorted(head = [1,2,1,2]))
    print(sol.deleteDuplicatesUnsorted(head = [3,2,2,1,3,2,4]))

if __name__ == "__main__": main()