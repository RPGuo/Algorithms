import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return []
        points = []
        for l, r, h in buildings:
            points.append((l, -h, r))
            points.append((r, h, 0))

        points.sort()
        height_heap = [[0, float('inf')]]
        res = [(0, 0)]

        for x, h, r in points:
            while x >= height_heap[0][1]:
                heapq.heappop(height_heap)
            if h < 0:
                heapq.heappush(height_heap, [h, r])
            if res[-1][1] != -height_heap[0][0]:
                res.append([x, -height_heap[0][0]])
        return res[1:]