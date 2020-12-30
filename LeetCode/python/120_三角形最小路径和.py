class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = triangle[row-1]
        for i in range(row-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]