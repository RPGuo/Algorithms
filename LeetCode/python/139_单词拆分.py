class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        max_len = max([len(x) for x in wordDict])

        breakp = [0]

        for i in range(len(s) + 1):
            if i - breakp[0] > max_len:
                breakp.pop(0)
                if not breakp:
                    return False
            for j in breakp:
                if s[j:i] in wordDict:
                    breakp.append(i)
                    break
        return breakp[-1] == len(s)