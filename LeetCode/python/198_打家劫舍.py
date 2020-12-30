class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        f0, f1 = 0, nums[0]
        for i in nums[1:]:
            f0, f1 = f1, max(f0+i, f1)
        return f1