class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for intv in intervals[1:]:
            last = res[-1]
            if intv[0] <= last[1]:
                last[1] = max(last[1], intv[1])
            else:
                res.append(intv)
        return res