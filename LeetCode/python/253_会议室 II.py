class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        for intev in intervals[1:]:
            if heap[0] <= intev[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intev[1])
        return len(heap)