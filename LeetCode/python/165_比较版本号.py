class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        i, j =0, 0
        while i < len(v1) or j < len(v2):
            char1 = int(v1[i]) if i < len(v1) else 0
            char2 = int(v2[j]) if j < len(v2) else 0
            if char1 == char2:
                i += 1
                j += 1
            elif char1 > char2:
                return 1
            else:
                return -1
        return 0