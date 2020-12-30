# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        fix = 0xffffffff
        while num2:
            temp = num1
            num1 = (temp ^ num2) & fix
            num2 = ((temp & num2) << 1) & fix
        # num1是原码表示，python的~操作会将结果按照补码输出结果
        return num1 if num1 <= 0x7fffffff else ~(num1 ^ fix)