class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, temp = nums[0], nums[0]
        for i in nums[1:]:
            if temp > 0:
                temp += i
            else:
                temp = i
            res = max(temp, res)
        return res