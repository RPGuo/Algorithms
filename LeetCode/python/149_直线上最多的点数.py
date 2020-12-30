class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import Counter
        points_dict = Counter(tuple(point) for point in points)
        not_repeat_point = list(points_dict.keys())
        n = len(not_repeat_point)
        if n == 1:
            return points_dict[not_repeat_point[0]]
        res = 0
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)
        for i in range(n-1):
            x1, y1 = not_repeat_point[i][0], not_repeat_point[i][1]
            slope = {}
            for j in range(i+1, n):
                x2, y2 = not_repeat_point[j][0], not_repeat_point[j][1]
                dy, dx = y2-y1, x2-x1
                g = gcd(dy, dx)
                if g != 0:
                    dy //= g
                    dx //= g
                slope["{}/{}".format(dy, dx)] = slope.get("{}/{}".format(dy, dx), 0) + points_dict[not_repeat_point[j]]
            res = max(res, max(slope.values()) + points_dict[not_repeat_point[i]])
        return res