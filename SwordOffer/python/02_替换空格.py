# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return ""
        res = []
        for i in s:
            if i == ' ':
                res.append('%20')
            else:
                res.append(i)
        return ''.join(res)