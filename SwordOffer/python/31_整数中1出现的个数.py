# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        m, res = 1, 0
        while m <= n:
            a = n//m
            b = n%m
            res += (a+8)//10*m + (a%10 == 1)*(b + 1)
            m = m*10
        return res