# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        pre, cur = dummy, head
        while cur:
            while cur and cur.next and cur.val == cur.next.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
            pre.next = cur
            pre = cur
            if not cur:
                break
            cur = cur.next
        return dummy.next