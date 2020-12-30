class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needs, windows = {}, {}
        left, right = 0, 0
        start, res = 0, float('inf')
        match = 0
        for temp in t:
            needs[temp] = needs.get(temp, 0) + 1
        while right < len(s):
            if s[right] in needs:
                windows[s[right]] = windows.get(s[right], 0) + 1
                if windows[s[right]] == needs[s[right]]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left < res:
                    start = left
                    res = right - left
                if s[left] in needs:
                    windows[s[left]] -= 1
                    if windows[s[left]] < needs[s[left]]:
                        match -= 1
                left += 1
        return s[start:start+res] if res != float('inf') else ''