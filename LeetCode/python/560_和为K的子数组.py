class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum = {}
        pre_sum[0] = 1
        res = 0
        sum_i = 0
        for i in range(len(nums)):
            sum_i += nums[i]
            sum_temp = sum_i - k
            if sum_temp in pre_sum:
                res += pre_sum[sum_temp]
            pre_sum[sum_i] = pre_sum.get(sum_i, 0) + 1
        return res