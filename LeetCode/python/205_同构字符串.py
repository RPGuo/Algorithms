class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def helper(s, t):
            dic = {}
            for i in range(len(s)):
                char_s, char_t = s[i], t[i]
                if char_s in dic:
                    if dic[char_s] != char_t:
                        return False
                else:
                    dic[char_s] = char_t
            return True

        return helper(s, t) and helper(t, s)