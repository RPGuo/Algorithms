# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        cur = res
        s = 0
        while l1 or l2 or s:
            value_l1 = l1.val if l1 else 0
            value_l2 = l2.val if l2 else 0
            value = s + value_l1 + value_l2
            s = value // 10
            value = value % 10

            cur.next = ListNode(value)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next