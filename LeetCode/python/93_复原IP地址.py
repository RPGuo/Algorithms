class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def helper(i, temp, flag):
            if i == n and flag == 0:
                res.append(temp[:-1])
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == '0':
                        helper(j + 1, temp + s[j] + '.', flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        helper(j + 1, temp + s[i:j + 1] + '.', flag - 1)

        helper(0, "", 4)
        return res