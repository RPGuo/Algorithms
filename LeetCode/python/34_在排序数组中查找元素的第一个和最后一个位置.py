class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        return [self.get_first(nums, target), self.get_last(nums, target)]

    def get_first(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if l == len(nums):
            return -1
        return l if nums[l] == target else -1

    def get_last(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        if r == 0:
            return -1
        return r - 1 if nums[r - 1] == target else -1