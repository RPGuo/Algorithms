class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp_0, dp_1 = 0, float('-inf')
        for i in range(len(prices)):
            temp = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, temp - prices[i] - fee)
        return dp_0