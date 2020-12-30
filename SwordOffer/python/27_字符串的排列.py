# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res = []
        self.cau(ss, res, '')
        return sorted(set(res))
    def cau(self, ss, res, path):
        if not ss:
            res.append(path)
        for i in range(len(ss)):
            self.cau(ss[:i]+ss[i+1:], res, path+ss[i])