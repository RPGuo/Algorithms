# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        con = list(range(n))
        start, final = 0, -1
        while con:
            k = (start + m - 1) % n
            final = con.pop(k)
            start = k
            n -= 1
        return final