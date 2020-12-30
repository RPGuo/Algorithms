### dp
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s))]
        res = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = (dp[i-2] if i-2>=0 else 0) + 2
                elif i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0) + 2
            res = max(res, dp[i])
        return res

### stack
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, res = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                stack.pop()
                if stack:
                    res = max(res, i-stack[-1])
                else:
                    stack.append(i)
        return res

### 特殊方法：左右遍历
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2*right)
            elif left < right:
                left = right = 0

        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2*right)
            elif left > right:
                left = right = 0
        return res