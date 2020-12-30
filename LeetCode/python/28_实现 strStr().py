class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(haystack)
        m = len(needle)
        i, j = 0 ,0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if(j >= m):
                    return i - j
            else:
                i = i - j + 1
                j = 0
        return -1