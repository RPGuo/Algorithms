class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        dp = [1]
        for i in range(1, rowIndex + 1):
            dp.insert(0, 0)
            for j in range(i):
                dp[j] = dp[j] + dp[j + 1]
        return dp