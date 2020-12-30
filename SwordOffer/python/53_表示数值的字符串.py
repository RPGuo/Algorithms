# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        hasE = hasDot = False
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-':
                if i > 0 and s[i-1] != 'E' and s[i-1] != 'e':
                    return False
            elif s[i] == 'E' or s[i] == 'e':
                if hasE or i == 0 or i == len(s) - 1:
                    return False
                hasE = True
            elif s[i] == '.':
                if hasE or hasDot:
                    return False
                hasDot = True
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True