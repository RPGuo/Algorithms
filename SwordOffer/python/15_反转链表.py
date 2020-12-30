# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
### 递归
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        head = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return head
### 迭代
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre, cur = None, pHead
        while cur:
            temp_next = cur.next
            cur.next = pre
            pre = cur
            cur = temp_next
        return pre