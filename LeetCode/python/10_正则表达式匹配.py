class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        row, col = len(s), len(p)
        dp = [[None for _ in range(col+1)] for _ in range(row+1)]
        dp[row][col] = True
        for i in range(row, -1, -1):
            for j in range(col-1, -1, -1):
                first = i < row and p[j] in {s[i], '.'}
                if j <= col - 2 and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first and dp[i+1][j]
                else:
                    dp[i][j] = first and dp[i+1][j+1]
        return dp[0][0]