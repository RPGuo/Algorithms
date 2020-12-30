class Solution:
    def countAndSay(self, n: int) -> str:
        pre = "1"
        for i in range(1, n):
            next = ''
            char, count = pre[0], 1
            for j in pre[1:]:
                if char == j:
                    count += 1
                else:
                    next += str(count) + char
                    char = j
                    count = 1
            next += str(count) + char
            pre = next
        return pre
