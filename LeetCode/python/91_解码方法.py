class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        pre = 1
        cur = 1
        for i in range(1, n):
            if s[i] == '0':
                # 310
                if s[i-1] == '1' or s[i-1] == '2':
                    cur = pre
                else:
                    return 0
            else:
                # 319
                if (s[i-1] == '1') or (s[i-1] == '2' and '0' <= s[i] <= '6'):
                    pre, cur = cur, pre + cur
                else:
                    pre = cur
        return cur