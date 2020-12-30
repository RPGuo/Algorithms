class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack, res = [], 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                res = max(res, (i-stack[-1]-1)*heights[temp])
            stack.append(i)
        return res