### dp
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_max = float('inf')
        dp = [num_max for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(i ** 0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]

### BFS
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue, step, visited = [n], 0, set()
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                temp = queue.pop(0)
                for i in range(1, int(temp ** 0.5) + 1):
                    diff = temp - i ** 2
                    if diff == 0:
                        return step
                    else:
                        if diff not in visited:
                            visited.add(diff)
                            queue.append(diff)
        return step