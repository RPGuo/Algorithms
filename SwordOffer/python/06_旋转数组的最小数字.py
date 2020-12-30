# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        nums = rotateArray
        if not nums:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]