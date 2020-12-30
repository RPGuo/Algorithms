# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = ListNode(-1)
        res.next = head
        pre = tail = res
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            next_head = pre.next
            while pre.next != tail:
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
            pre = tail = next_head
        return res.next