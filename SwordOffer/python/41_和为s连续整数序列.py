# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        l, r, res = 1, 2, []
        while l < r:
            temp = (l+r)*(r-l+1)/2
            if temp < tsum:
                r += 1
            elif temp > tsum:
                l += 1
            else:
                res.append(range(l,r+1))
                l += 1
        return res