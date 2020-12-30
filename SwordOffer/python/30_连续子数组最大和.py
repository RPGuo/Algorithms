# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        cur = 0
        great_sum = -0xffffffff
        for i in array:
            if cur <= 0:
                cur = i
            else:
                cur += i
            if great_sum < cur:
                great_sum = cur
        return great_sum