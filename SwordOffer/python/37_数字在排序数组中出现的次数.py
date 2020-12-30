# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        return self.get_last(data, k) - self.get_first(data, k) + 1

    def get_first(self, data, k):
        l = 0
        r = len(data) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if data[mid] < k:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def get_last(self, data, k):
        l = 0
        r = len(data) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if data[mid] <= k:
                l = mid + 1
            else:
                r = mid - 1
        return r