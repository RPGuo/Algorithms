# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        return self.sol(data)[1]%1000000007
    def sol(self, data):
        if not data or len(data) == 1:
            return data, 0
        mid = len(data) // 2
        l_res, l_count = self.sol(data[:mid])
        r_res, r_count = self.sol(data[mid:])
        res, count = self.merged(l_res, r_res)
        return res, l_count + r_count + count
    def merged(self, left, right):
        l, r = 0, 0
        res = []
        count = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
                count += len(left) - l
        res += left[l:] if left[l:] else right[r:]
        return res, count