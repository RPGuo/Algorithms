class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return nums
        n, flag = len(nums), False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                flag = True
                break
        if not flag:
            self.reverse(nums, 0, n - 1)
            return nums
        for j in range(n - 1, i, -1):
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1, n - 1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1