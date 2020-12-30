class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            s1 = self.helper(s, i, i)
            s2 = self.helper(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
    def helper(self, s, l , r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

### manacher
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s
        str1 = self.pre_process(s)
        p_arr = [0]*len(str1)
        max_len, max_str = float('-inf'), ''
        c = r = -1
        for i in range(len(str1)):
            p_arr[i] = min(p_arr[2*c - i], r-i) if i < r else 1
            while i + p_arr[i] < len(str1) and i - p_arr[i] >= 0:
                if str1[i + p_arr[i]] == str1[i - p_arr[i]]:
                    p_arr[i] += 1
                else:
                    break
            if i + p_arr[i] > r:
                r = i + p_arr[i]
                c = i
            if max_len < p_arr[i]:
                max_len = p_arr[i]
                temp_start = (i - max_len + 1) // 2
                max_str = s[temp_start:temp_start+max_len-1]
        return max_str

    def pre_process(self, str1):
        fill_char = '#'
        str1 = list(str1)
        res = [fill_char]
        for char in str1:
            res.append(char)
            res.append(fill_char)
        return ''.join(res)