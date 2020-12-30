# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k<=0 or len(tinput) < k:
            return []
        l = 0
        r = len(tinput) - 1
        while True:
            index = self.patition(tinput, l, r)
            if index > k - 1:
                r = index - 1
            elif index < k - 1:
                l = index + 1
            else:
                return sorted(tinput[:index+1])
    def patition(self, tinput, l, r):
        key = tinput[l]
        while l < r:
            while l < r and key <= tinput[r]:
                r -= 1
            tinput[l] = tinput[r]
            while l < r and key >= tinput[l]:
                l += 1
            tinput[r] = tinput[l]
        tinput[l] = key
        return l