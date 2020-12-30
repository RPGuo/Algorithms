# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.res = []
        self.dict = {}
    def FirstAppearingOnce(self):
        # write code here
        while self.res and self.dict[self.res[0]] > 1:
            self.res.pop(0)
        if self.res:
            return self.res[0]
        else:
            return '#'
    def Insert(self, char):
        # write code here
        try:
            self.dict[char] += 1
        except:
            self.dict[char] = 1
            self.res.append(char)