class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1 == 1:
            return False
        target = s // 2
        dp = [False for _ in range(target + 1)]
        for j in range(target+1):
            dp[j] = False if nums[0] != j else True
        for i in range(1, len(nums)):
            for j in range(target, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]