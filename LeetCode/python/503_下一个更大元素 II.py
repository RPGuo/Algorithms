class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack, res = [], [-1] * n
        for i in range(2*n-1, -1, -1):
            ### 找下一个更大，相等也必须pop
            while stack and nums[i%n] >= stack[-1]:
                stack.pop()
            res[i%n] = stack[-1] if stack else -1
            stack.append(nums[i%n])
        return res