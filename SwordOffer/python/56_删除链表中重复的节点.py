# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        res = ListNode(0)
        res.next = pHead
        pre = res
        cur = pHead
        while cur and cur.next:
            temp = cur.next
            if cur.val == temp.val:
                while temp and temp.val == cur.val:
                    temp = temp.next
                pre.next = temp
                cur = temp
            else:
                pre = cur
                cur = cur.next
        return res.next