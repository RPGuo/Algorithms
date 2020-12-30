class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if k > len(prices) // 2:
            return self.k_inf(prices)
        else:
            return self.k_any(prices, k)

    def k_inf(self, prices):
        dp_0, dp_1 = 0, float('-inf')
        for i in range(len(prices)):
            temp = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, temp - prices[i])
        return dp_0

    def k_any(self, prices, k_max):
        dp = [[[0, 0] for _ in range(k_max + 1)] for _ in range(len(prices) + 1)]
        for k in range(k_max + 1):
            dp[0][k][1] = float('-inf')
        for i in range(len(prices) + 1):
            dp[i][0][1] = float('-inf')
        for i in range(1, len(prices) + 1):
            for k in range(1, k_max + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i - 1])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i - 1])
        return dp[-1][-1][0]