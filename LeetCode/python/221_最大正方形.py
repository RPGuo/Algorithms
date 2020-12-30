class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        heights = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            res = max(res, self.helper(heights))
        return res

    def helper(self, heights):
        stack, res = [], 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                length = min(heights[temp], i - stack[-1] - 1)
                res = max(res, length * length)
            stack.append(i)
        return res