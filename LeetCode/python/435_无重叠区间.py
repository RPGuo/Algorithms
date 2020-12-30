class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or len(intervals) < 2:
            return 0
        self.sort_by_end(intervals, 0, len(intervals) - 1)
        res = 1
        temp = intervals[0]
        for inter in intervals[1:]:
            if inter[0] >= temp[1]:
                res += 1
                temp = inter
        return len(intervals) - res

    def sort_by_end(self, intervals, left, right):
        if left >= right:
            return
        key = intervals[left]
        l = left
        r = right
        while l < r:
            while l < r and intervals[r][1] >= key[1]:
                r -= 1
            intervals[l] = intervals[r]
            while l < r and intervals[l][1] <= key[1]:
                l += 1
            intervals[r] = intervals[l]
        intervals[l] = key
        self.sort_by_end(intervals, left, l - 1)
        self.sort_by_end(intervals, l + 1, right)