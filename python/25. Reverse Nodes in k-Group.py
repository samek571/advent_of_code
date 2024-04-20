class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''we use stack to reverse nodes in groups, first we get the lenght of the ls
    to not perform swappage in the last remainders of n%k < k'''
    def reverseKGroup(self, head, k: int):# -> Optional[ListNode]:

		# total count of linked-lists
        cur = head
        remain_count = 0
        while cur:
            cur = cur.next
            remain_count += 1

        cur = head
        head = ListNode()
        pre = head

        stack = []
        while remain_count >= k:
            batch_count = k
            while batch_count:
                stack.append(cur)
                cur = cur.next
                batch_count -= 1
            nxt = cur

            while len(stack):
                cur = stack.pop()
                pre.next = cur
                pre = pre.next
            cur = nxt

            remain_count -= k

        pre.next = cur if remain_count else None
        return head.next


def main():
    sol = Solution()
    print(sol.reverseKGroup(ListNode([1,2,3,4,5]), 2))

if __name__ == "__main__": main()
