# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        f1 = 1
        f2 = 2
        if number <= 0:
            return 0
        for i in range(number-1):
            f1, f2 = f2, f1 + f2
        return f1