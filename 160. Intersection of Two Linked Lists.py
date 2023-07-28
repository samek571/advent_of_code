# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, first: ListNode, second: ListNode):# -> Optional[ListNode]:
        # if not first or not second: return 0

        # da, db = first, second

        # while da != db:
        #     da = second if not da else da.next
        #     db = first if not db else db.next

        # return da

        seen = set()

        da, db = first, second

        while da:
            seen.add(da)
            da = da.next

        while db:
            if db in seen: return db
            db = db.next

        return
