class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or k < 0:
            return []
        k = k % len(nums)
        self.swap(nums, 0, len(nums) - 1)
        self.swap(nums, 0, k - 1)
        self.swap(nums, k, len(nums) - 1)
        return nums

    def swap(self, temp, l, r):
        while l < r:
            temp[l], temp[r] = temp[r], temp[l]
            l += 1
            r -= 1