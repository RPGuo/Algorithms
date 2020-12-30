class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S)&1 == 1:
            return 0
        target = (sum(nums) + S) // 2
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] += dp[j-num]
        return dp[target]