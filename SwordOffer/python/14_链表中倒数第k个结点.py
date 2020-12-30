# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        fast = head
        for _ in range(k-1):
            fast = fast.next
            if not fast:
                return None
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow