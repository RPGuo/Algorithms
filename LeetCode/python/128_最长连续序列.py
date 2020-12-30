class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp, res = set(), 0
        for i in nums:
            temp.add(i)
        for i in temp:
            if i-1 not in temp:
                count = 0
                while i in temp:
                    i += 1
                    count += 1
                res = max(res, count)
        return res