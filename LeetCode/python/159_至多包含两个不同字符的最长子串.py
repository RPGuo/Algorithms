class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, hash_map, dist = 0, {}, 0
        i = 0
        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]] += 1
            else:
                hash_map[s[j]] = 1
                dist += 1
                while dist > 2:
                    hash_map[s[i]] -= 1
                    if hash_map[s[i]] == 0:
                        dist -= 1
                        hash_map.pop(s[i])
                    i += 1
            res = max(res, j - i + 1)
        return res