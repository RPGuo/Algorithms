# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def __init__(self):
        self.small = []
        self.large = []
        self.count = 0
    def Insert(self, num):
        # write code here
        self.count += 1
        if self.count&1 == 1:
            heappush(self.large, num)
            heappush(self.small, -heappop(self.large))
        else:
            heappush(self.small, -num)
            heappush(self.large, -heappop(self.small))
    def GetMedian(self, n):
        # write code here
        if self.count&1 == 1:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0