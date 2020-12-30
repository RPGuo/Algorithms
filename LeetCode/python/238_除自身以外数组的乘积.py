class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0 for _ in range(n)]
        k = 1
        for i in range(n):
            res[i] = k
            k = k * nums[i]
        k = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * k
            k = k * nums[i]
        return res