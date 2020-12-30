class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        max_step = nums[0]
        for i in range(1, len(nums)):
            if i > max_step:
                return False
            max_step = max(max_step, i + nums[i])
        return True