# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        head1 = pHead1
        head2 = pHead2
        while head1 != head2:
            head1 = head1.next if head1 else pHead2
            head2 = head2.next if head2 else pHead1
        return head1