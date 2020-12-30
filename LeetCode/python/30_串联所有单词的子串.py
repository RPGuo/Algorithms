from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(one_word):
            cur_num = 0
            left = i
            right = i
            cur_words = Counter()
            while right + one_word <= n:
                w = s[right: right + one_word]
                cur_words[w] += 1
                cur_num += 1
                right += one_word
                while cur_words[w] > words[w]:
                    left_w = s[left:left + one_word]
                    cur_words[left_w] -= 1
                    cur_num -= 1
                    left += one_word
                if cur_num == word_num:
                    res.append(left)
        return res