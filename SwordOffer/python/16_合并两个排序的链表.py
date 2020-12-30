# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
### 循环
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return pHead1 if pHead1 else pHead2
        dummy = ListNode(-1)
        cur = dummy
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        cur.next = pHead1 if pHead1 else pHead2
        return dummy.next

### 递归
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return pHead1 if pHead1 else pHead2
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2