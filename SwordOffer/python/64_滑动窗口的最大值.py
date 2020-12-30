# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size < 1:
            return []
        temp_index, res = [], []
        for i in range(len(num)):
            if temp_index and i - temp_index[0] + 1 > size:
                temp_index.pop(0)
            while temp_index and num[i] > num[temp_index[-1]]:
                temp_index.pop()
            temp_index.append(i)
            if i+1 >= size:
                res.append(num[temp_index[0]])
        return res