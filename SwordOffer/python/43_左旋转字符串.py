# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        if n < 0:
            return ''
        s = list(s)
        self.inverse(s, 0, n-1)
        self.inverse(s, n, len(s)-1)
        self.inverse(s, 0, len(s)-1)
        return ''.join(s)
    def inverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1