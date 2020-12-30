# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        f1 = 0
        f2 = 1
        for i in range(n):
            f1, f2 = f2, f1 + f2
        return f1