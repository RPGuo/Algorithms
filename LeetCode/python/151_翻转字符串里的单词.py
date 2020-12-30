class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)

        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        def word_reverse(s):
            i = 0
            j = 0
            while i < n:
                while i < n and s[i] == ' ':
                    i += 1
                j = i
                while j < n and s[j] != ' ':
                    j += 1
                reverse(s, i, j - 1)
                i = j

        def clean_space(s):
            i = 0
            j = 0
            while j < n:
                while j < n and s[j] == ' ':
                    j += 1
                while j < n and s[j] != ' ':
                    s[i] = s[j]
                    i += 1
                    j += 1
                while j < n and s[j] == ' ':
                    j += 1
                if j < n:
                    s[i] = ' '
                    i += 1
            return ''.join(s[:i])

        reverse(s, 0, n - 1)
        word_reverse(s)
        return clean_space(s)