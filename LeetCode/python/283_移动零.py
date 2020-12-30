class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                if i != j:
                    nums[i] = nums[j]
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1