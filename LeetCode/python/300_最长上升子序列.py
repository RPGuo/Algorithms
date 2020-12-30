class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res

# O(nlog(n))
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                mid = (i+j) // 2
                if tail[mid] < num:
                    i = mid+1
                else:
                    j = mid
            tail[i] = num
            if j == res:
                res += 1
        return res