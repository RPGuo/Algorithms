# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        i = len(array) - 1
        j = 0
        while i >= 0 and j <= len(array[0]) - 1:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False