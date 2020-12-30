class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict1 = {}
        for item in s:
            dict1[item] = dict1.get(item, 0) + 1
        for item in t:
            if item not in dict1 or dict1[item] <= 0:
                return False
            dict1[item] -= 1
        return True
