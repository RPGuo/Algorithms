class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for j in range(2, len(nums)):
            for i in range(j-2, -1, -1):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[k] * nums[i] * nums[j])
        return dp[0][-1]