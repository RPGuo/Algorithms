class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, res = 0, 0, 0
        windows = {}
        while right < len(s):
            temp = s[right]
            windows[temp] = windows.get(temp, 0) + 1
            while windows[temp] > 1:
                windows[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res