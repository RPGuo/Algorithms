# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        cur = pHead
        while cur:
            temp = RandomListNode(cur.label)
            temp.next = cur.next
            cur.next = temp
            cur = cur.next.next
        cur = pHead
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        cur = pHead
        res = pHead.next
        while cur:
            temp = cur.next
            cur.next = temp.next
            temp.next = temp.next.next if temp.next else None
            cur = cur.next
        return res