class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        repre = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for i in range(len(value)):
            while num >= value[i]:
                num -= value[i]
                res += repre[i]
        return res