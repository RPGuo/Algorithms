class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

### 排列组合
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num = m + n - 2
        k = m - 1
        res = 1
        for i in range(1, k+1):
            res = res*(num-k+i)/i
        return int(res)