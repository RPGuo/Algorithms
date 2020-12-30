# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent > 0:
            n = exponent
        elif exponent < 0:
            if base == 0:
                return -1
            else:
                n = -exponent
        else:
            if base == 0:
                return -1
            else:
                return 1
        res = 1
        temp = base
        while n:
            if n&1 == 1:
                res = res * temp
            temp = temp * temp
            n = n >> 1
        return res if exponent > 0 else 1.0/res