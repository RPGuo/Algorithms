# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        s = list(s.split(" "))
        self.inverse(s, 0, len(s)-1)
        return ' '.join(s)
    def inverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1