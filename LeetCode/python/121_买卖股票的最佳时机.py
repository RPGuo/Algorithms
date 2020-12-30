# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices:
#             return 0
#         res, cur_min = 0, prices[0]
#         for i in range(1, len(prices)):
#             cur_min = min(cur_min, prices[i])
#             res = max(res, prices[i]-cur_min)
#         return res

### 通用解法
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp_0, dp_1 = 0, float('-inf')
        for i in range(0, len(prices)):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, -prices[i])
        return dp_0