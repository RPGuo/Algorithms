class Solution:
    def minCut(self, s: str) -> int:
        min_cut = [ i for i in range(len(s))]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if i == 0:
                        min_cut[j] = 0
                    else:
                        min_cut[j] = min(min_cut[j], min_cut[i-1] + 1)
        return min_cut[-1]