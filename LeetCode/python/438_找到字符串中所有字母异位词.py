class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        needs, windows = {}, {}
        left, right = 0, 0
        res, match = [], 0
        for temp in p:
            needs[temp] = needs.get(temp, 0) + 1
        while right < len(s):
            if s[right] in needs:
                windows[s[right]] = windows.get(s[right], 0) + 1
                if windows[s[right]] == needs[s[right]]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left == len(p):
                    res.append(left)
                if s[left] in needs:
                    windows[s[left]] -= 1
                    if windows[s[left]] < needs[s[left]]:
                        match -= 1
                left += 1
        return res