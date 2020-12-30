# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        flag = 0
        if s[0] == '+':
            flag = 1
            s = s[1:]
        elif s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] in num_list:
            flag = 1
            s = s
        else:
            return 0
        res = 0
        for i in s:
            if i in num_list:
                res = res*10 + num_list.index(i)
            else:
                return 0
        return res*flag