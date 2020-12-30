class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        if not words or maxWidth < 0:
            return ""

        s, temp = [], []
        l = 0
        for word in words:
            if l + len(word) <= maxWidth:
                l = l + len(word) + 1
                temp.append(word)
            else:
                s.append(temp)
                l = len(word) + 1
                temp = [word]
        s.append(temp)

        res = []
        a = ' '
        for word_s in s[:-1]:
            if len(word_s) == 1:
                res.append(word_s[0] + a * (maxWidth - len(word_s[0])))
            elif len(word_s) == 2:
                res.append(word_s[0] + a * (maxWidth - len(word_s[0]) - len(word_s[1])) + word_s[1])
            else:
                sum_len = sum([len(i) for i in word_s])
                m = (maxWidth - sum_len) // (len(word_s) - 1)
                n = (maxWidth - sum_len) % (len(word_s) - 1)
                temp_res = word_s[0]
                i = 1
                while i < len(word_s):
                    if n > 0:
                        temp_res += a * m + a + word_s[i]
                    else:
                        temp_res += a * m + word_s[i]
                    i += 1
                    n -= 1
                res.append(temp_res)

        temp_res = s[-1][0]
        for i in range(1, len(s[-1])):
            temp_res += a + s[-1][i]
        temp_res += a * (maxWidth - len(temp_res))
        res.append(temp_res)
        return res