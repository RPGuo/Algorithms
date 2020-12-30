class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
### 通用解法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_0, dp_1 = 0, float('-inf')
        for i in range(len(prices)):
            temp = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, temp - prices[i])
        return dp_0