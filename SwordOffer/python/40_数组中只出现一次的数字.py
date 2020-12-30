# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []
        temp = 0
        for i in array:
            temp ^= i
        count = 0
        while temp & 1==0:
            count += 1
            temp = temp >> 1
        a, b = 0, 0
        for i in array:
            if i>>count&1==0:
                a ^= i
            else:
                b ^= i
        return [a, b]