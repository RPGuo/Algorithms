# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        l, r = 0, len(array)-1
        res = []
        while l < r:
            temp = array[l] + array[r]
            if temp < tsum:
                l += 1
            elif temp > tsum:
                r -= 1
            else:
                res.append(array[l])
                res.append(array[r])
                break
        return res