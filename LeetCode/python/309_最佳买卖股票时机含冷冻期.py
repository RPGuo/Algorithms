class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_0, dp_1 = 0, float('-inf')
        dp_pre = 0
        for i in range(len(prices)):
            temp = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, dp_pre - prices[i])
            dp_pre = temp
        return dp_0