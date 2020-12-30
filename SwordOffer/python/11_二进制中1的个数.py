# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n&0xffffffff
        res = 0
        while n:
            res += 1
            n = n&(n-1)
        return res