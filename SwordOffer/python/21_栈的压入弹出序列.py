# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        if len(pushV) != len(popV):
            return False
        stack = []
        while pushV:
            stack.append(pushV.pop(0))
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return True if not stack else False