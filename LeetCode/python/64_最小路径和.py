class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = grid[i][n - 1] + dp[i + 1][n - 1]
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = grid[m - 1][j] + dp[m - 1][j + 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
### 不需要额外空间
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                elif i==0 and j!=0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif i!=0 and j==0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]