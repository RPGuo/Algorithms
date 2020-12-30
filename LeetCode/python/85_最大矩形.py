class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] = heights[j] + 1
            res = max(res, self.helper(heights))
        return res
    def helper(self, heights):
        stack, res = [], 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                res = max(res, heights[temp] * (i-stack[-1]-1))
            stack.append(i)
        return res