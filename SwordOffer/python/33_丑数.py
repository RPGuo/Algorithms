# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        res = [1]
        index2, index3, index5 = 0, 0, 0
        for i in range(index-1):
            res.append(min(res[index2]*2, res[index3]*3, res[index5]*5))
            while res[index2]*2 <= res[-1]:
                index2 += 1
            while res[index3]*3 <= res[-1]:
                index3 += 1
            while res[index5]*5 <= res[-1]:
                index5 += 1
        return res[-1]