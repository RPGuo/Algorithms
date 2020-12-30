class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k < 1 or k > len(nums):
            return 0
        k = len(nums) - k + 1
        return self.qs(nums, 0, len(nums) - 1, k)

    def qs(self, nums, left, right, k):
        l, r = left, right
        key = nums[l]
        while l < r:
            while l < r and nums[r] >= key:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= key:
                l += 1
            nums[r] = nums[l]
        nums[l] = key

        if l == k - 1:
            return nums[l]
        elif l > k - 1:
            return self.qs(nums, left, l - 1, k)
        else:
            return self.qs(nums, l + 1, right, k)