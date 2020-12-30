class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and self.helper(s[l]):
                l += 1
            l_char = s[l].lower()
            while l < r and self.helper(s[r]):
                r -= 1
            r_char = s[r].lower()
            if l_char != r_char:
                return False
            r -= 1
            l += 1
        return True

    def helper(self, char):
        return not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9')