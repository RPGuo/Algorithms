class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            x = i % 2
            y = (i-1) % 2
            dp[x][0] = max(dp[y][0]*nums[i], dp[y][1]*nums[i], nums[i])
            dp[x][1] = min(dp[y][0]*nums[i], dp[y][1]*nums[i], nums[i])
            res = max(res, dp[x][0])
        return res