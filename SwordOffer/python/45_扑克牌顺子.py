# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        temp = {}
        _min, _max = 54, -1
        for i in numbers:
            if i == 0:
                continue
            try:
                temp[i] += 1
            except:
                temp[i] = 1
            if temp[i] > 1:
                return False
            if _min > i:
                _min = i
            if _max < i:
                _max = i
        return True if (_max-_min) < 5 else False