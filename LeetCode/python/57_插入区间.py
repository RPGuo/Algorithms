class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def helper():
            left = 0
            right = len(intervals)
            while left < right:
                mid = (left + right) >> 1
                if intervals[mid][0] < newInterval[0]:
                    left = left + 1
                else:
                    right = mid
            return left

        i = helper()
        intervals.insert(i, newInterval)
        while i + 1 < len(intervals) and intervals[i + 1][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], intervals.pop(i + 1)[1])
        if i - 1 >= 0 and intervals[i - 1][1] >= intervals[i][0]:
            intervals[i - 1][1] = max(intervals[i - 1][1], intervals.pop(i)[1])
        return intervals