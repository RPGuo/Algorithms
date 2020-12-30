class Solution:
    def decodeString(self, s: str) -> str:
        res, multi, stack = "", 0, []
        for char in s:
            if char == "[":
                stack.append([multi, res])
                multi = 0
                res = ""
            elif char == "]":
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= char <= '9':
                multi = multi * 10 + int(char)
            else:
                res += char
        return res