# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        stack = []
        head = pre = None
        cur = pRootOfTree
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not pre:
                head = cur
            else:
                pre.right = cur
                cur.left = pre
            pre = cur
            cur = cur.right
        return head