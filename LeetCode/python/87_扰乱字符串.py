class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if len(s1) != len(s2):
            return False
        n = len(s1)
        dp = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    if length == 1:
                        dp[length][i][j] = True if s1[i] == s2[j] else False
                    else:
                        for q in range(1, length):
                            dp[length][i][j] = (dp[q][i][j] and dp[length - q][i + q][j + q]) or (
                                        dp[q][i][j + length - q] and dp[length - q][i + q][j])
                            if dp[length][i][j]:
                                break
        return dp[n][0][0]