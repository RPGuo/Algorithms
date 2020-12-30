### memo
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        memo = {}
        def helper(start, end):
            res = 0
            if start >= end:
                return 1
            if (start, end) in memo:
                return memo[(start, end)]
            for i in range(start, end+1):
                left_num = helper(start, i-1)
                right_num = helper(i+1, end)
                res += left_num * right_num
            memo[(start, end)] = res
            return res
        return helper(1, n)

### dp
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                left = j - 1
                right = i - j
                dp[i] += dp[left] * dp[right]
        return dp[n]

### 改进dp
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            mid = i // 2
            for j in range(1, mid+1):
                left = j - 1
                right = i - j
                dp[i] += dp[left] * dp[right]
            dp[i] = dp[i]*2
            if i&1 == 1:
                node = mid + 1
                left = node-1
                right = i-node
                dp[i] += dp[left] * dp[right]
        return dp[n]
### 卡塔兰数列
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(1, n+1):
            res = res*(n+i)/i
        return int(res/(i+1))