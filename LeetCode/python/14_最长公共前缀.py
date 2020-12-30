class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for temp in zip(*strs):
            if len(set(temp)) == 1:
                res += temp[0]
            else:
                break
        return res