class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0
        while l <= r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if l_max < r_max:
                res += l_max - height[l]
                l += 1
            else:
                res += r_max - height[r]
                r -= 1
        return res