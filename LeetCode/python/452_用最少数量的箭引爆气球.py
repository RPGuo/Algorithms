class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        res = 1
        temp = points[0]
        for point in points[1:]:
            if point[0] > temp[1]:
                res += 1
                temp = point
        return res