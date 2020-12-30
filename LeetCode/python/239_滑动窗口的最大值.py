class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k < 1:
            return None
        res, index = [], []
        for i in range(len(nums)):
            if index and i - index[0] + 1 > k:
                index.pop(0)
            while index and nums[i] > nums[index[-1]]:
                index.pop()
            index.append(i)

            if i + 1 >= k:
                res.append(nums[index[0]])
        return res