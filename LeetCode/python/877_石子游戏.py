class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = (piles[i], 0)
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j] = (left, dp[i+1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j-1][0])
        return True if dp[0][n-1][0] > dp[0][n-1][1] else False

### 必胜
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True