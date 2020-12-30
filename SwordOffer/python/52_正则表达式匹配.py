# -*- coding:utf-8 -*-
### 递归
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not pattern:
            return not s
        first = s and pattern[0] in {s[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return self.match(s, pattern[2:]) or first and self.match(s[1:], pattern)
        else:
            return first and self.match(s[1:], pattern[1:])
### 递归加备忘录
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(pattern):
                return i == len(s)
            first = i < len(s) and pattern[j] in {s[i], '.'}
            if j <= len(pattern) - 2 and pattern[j+1] == '*':
                ans = dp(i, j+2) or first and dp(i+1, j)
            else:
                ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)