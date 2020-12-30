class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res, i = 0, 0
        re_dict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10,
                 'IX':9, 'V':5, 'IV':4, 'I':1}
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in re_dict:
                res += re_dict[s[i:i+2]]
                i += 2
            else:
                res += re_dict[s[i]]
                i += 1
        return res