class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y, res = abs(x), 0
        max_num, min_num = (1<<31)-1, (-1<<31)
        while y != 0:
            res = res*10 + y%10
            if res>max_num or res<min_num:
                return 0
            y = y//10
        return res if x>0 else -res